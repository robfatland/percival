import sys
from numpy import isnan
from datetime import datetime
from os import listdir
from os.path import isfile, join

#
# This program sorts out some VIC output into files suitable for import into WWT 
# In WWT you would set Look At = Earth, open the Layer Manager, right click, select Add, open the CSV file...
#   ...and there will be a pause of maybe 30 seconds while the data loads; talking about 590k values with typical parameters.
# From there you'll need to make some adjustments to the imported layer:
#   Select the new layer and click 'Time Series' so it knows it is time-enabled
#   Set the Properties to include a nice time delay value like 8 or 16 days
#   Right-click the layer and set the opacity to very faint to see the underlying terrain
#
# kilroy here are a few items that could be done better or explored
#   - by adding a lat and lon column to the output you can switch between column and marker representation;
#     in fact WWT allows you to have both on: Think column with beacon at the top for starters. 
#     This could facilitate comparison of two types, e.g. precip and evap. Also important would be a 
#     lat/lon-only (no GEOMETRY) option.
#   - drawing polygons CW versus CCW can have different effects... w/r/t LINESTRING / POLYGON
#   - dual data: placing layers at 200k meters as the pedestal (with LINESTRING) may actually obviate the need for relief because
#     at that height it just looks mostly like a shell where the color-coding is carrying most of the information. Anyway having
#     the option to put something Way Up There is a nice way of creating a differentiation / comparison context.
#   - unexplored idea: Make alt and color from different columns
#   - create pairs of indicators in each cell (splitting the real estate) but I doubt this will work.
#   - solid color (no altitude coding) would also give a simpler way of comparing two types. The easiest way to do this is in WWT
#       . turn off the color column
#       . right-click the layer and set a color for it (white by default)
#   - give the program some command line arguments

###################
#
# hardcoded configuration elements
#
###################

# choose precip = 3, evap = 4, runoff = 5, baseflow = 6
dataTypeIndex = 6

# command line arguments; pulled up from 'buried in the code'
# Data grab will commence on calendar year (1950 + yearsSkip)
yearsSkip = 3

# we read every (linesDaySkip + 1)'th day of data and skip the remainder
linesDaySkip = 2

# This code only gets a year or two of data
yearsGet = 1

# geographic grid spacing: hardcoded (kilroy) to be just under perfect
dlat = 0.08
dlon = 0.08

# a little modifying factor for artistic license: Will expand/contract the basic cell dimensions
latMag = 1.0
lonMag = 1.0

# turn this on (True) to drastically reduce number of polygons drawn
drawOnlySignificantData = True

# turn this on (True) to draw data as markers rather than as GEOMETRY Well Known Text
drawDataAsMarkers = True

# in the case where we don't want to draw "no precip" or "no runoff" or "no base flow" this threshold is used as the
#   cutoff. It doesn't really make sense for evap; a different scheme would be wanted there (and a different pedestal)
significanceThreshold = [0., 0., 0., 0.2, -10.0, 0.2, 0.01]

# pedestals correspond in indices 3, 4, 5 and 6 to respectively precip, evap (+/-), runoff and base flow
# They are altitudes in meters for displaying the data above the terrain in WWT
pedestals = [0., 0., 0., 6000.0, 200000.0, 6000.0, 6000.0]

# not used but anticipating choosing to put a shell version of a data type very high
shellPedestals = [0., 0., 0., 200000.0, 200000.0, 200000.0, 200000.0]

# component path and filename info
rootdir = "C:\\Users\\fatla_000\\Documents\\"
datadir = "Data\\"
domaindir = "Jeff Richey Brazil DIF\\"
qualifier = "fluxes"

# This part is a bit circuitous but it works from data type selection (see up top).
# We are pulling data from the list a[]: Column 3, 4, 5, or 6 (indexing from 0) 
# corresponding to precip / evap / runoff / base flow. So you have to choose one
# of those four indices: 3, 4, 5 or 6 as 'dataTypeIndex'. Everything follows from
# there. One may wish to modify the intrinsic scaling.
dataTypeScaleList = [0., 0., 0., 1000.0, 10000.0, 1000.0, 10000.0]
dataTypeNameList = ['year', 'month', 'day', 'precip', 'evap', 'runoff', 'baseflow']

# the color coding is based on the data column of interest (a3/a4/a5/a6) which becomes altitude
# it *could* be done based on a different column than the altitude at the risk of being confusing
colors = ['red','orange','green','cyan','blue','white']
nColors = len(colors)
colorIntervals = [0., 0., 0., 3000., 5000., 3000., 3000.]
colorInterval = colorIntervals[dataTypeIndex]


########################
#
# Derived values
# 
########################

# choose between MULTIPOLYGON and MULTILINESTRING: At the moment tied to the data type chosen...
geomType = 'MULTIPOLYGON'
if dataTypeIndex == 4: geomType = 'MULTILINESTRING'

# place the data on a pedestal to get it up above most of the topography
pedestal = pedestals[dataTypeIndex]

# For cases / indices 3, 5 and 6 the data are zero or positive so we simply work from the pedestal up.
# For case / index 4 = evap the data are positive or negative so we set a floor based on seven colors
floors = [0., 0., 0., pedestals[3], pedestals[4] - 3.0*colorIntervals[4], pedestals[5], pedestals[6]]
floor = floors[dataTypeIndex]

# used to calculate the color to use for a particular cell
colorDC = floor

# derived path info
fullpathdir = rootdir + datadir + domaindir

# The output file retains "type" (precip, runoff etc), "when" (year) and "how long" (in years) for this data subset
# For example you could get vicsort_runoff_1964_2.csv which is data from 1964 and 1965 (2 years)
outfileBase = 'vicsort_' + dataTypeNameList[dataTypeIndex] + '_' + str(1950 + yearsSkip) + '_' + str(yearsGet) + '_'

# Get the data-to-altitude scale factor from a list of them
dataTypeScale = dataTypeScaleList[dataTypeIndex]


########################
#
# Custom methods
#
########################

# Write a long list as a sequence of rows to a CSV file: customized for WWT with GEOMETRY / MULTIPOLYGON WKT
def WriteCSVFileWithGEOMETRY(file, longlist, header, dlonScale, dlatScale, geomType):
    # expect header to be GEOMETRY date altitude color for a total of five values since GEOM uses two
    entries_per_row = 5

    # How many rows we expect to write to the output file
    numRows = len(longlist) / entries_per_row

    # Check that the list length jives with the assumptions
    if numRows * entries_per_row != len(longlist):
        print "The long list does not parse evenly into expected entries per row!!!"
        sys.exit(0)

    # Take care of the top of the file
    f = open(file, 'w')
    f.write(header + '\n')

    # loop over the rows of the output file
    for i in range(numRows):

        # start is the index of this row's elements in the list
        start = i * entries_per_row

        # a/b are lon/lat corner coordinates
        a0 = str(longlist[start] - dlonScale)
        a1 = str(longlist[start] + dlonScale)
        b0 = str(longlist[start + 1] - dlatScale)
        b1 = str(longlist[start + 1] + dlatScale)

        # This is 'well known text' (WKT) and it draws a solid-color rectangle centered on the grid point
        geomEntry = geomType + '((' + a0 + ' ' + b0 + ',' + a1 + ' ' + b0 + ','
        geomEntry += a1 + ' ' + b1 + ',' + a0 + ' ' + b1 + ',' + a0 + ' ' + b0 + ')),'

        f.write(geomEntry)

        # Add in the date, the altitude and the color for this row
        f.write(str(longlist[start + 2]) + ',')
        f.write(str(longlist[start + 3]) + ',')
        f.write(str(longlist[start + 4]) + '\n')

    # and that's it
    f.close()

def WriteCSVFileWithLonLat(file, longlist, header):

    # expect header to be lon lat date altitude color for a total of five values
    entries_per_row = 5

    # How many rows we expect to write to the output file
    numRows = len(longlist) / entries_per_row

    # Check that the list length jives with the assumptions
    if numRows * entries_per_row != len(longlist):
        print "The long list does not parse evenly into expected entries per row!!!"
        sys.exit(0)

    # Take care of the top of the file
    f = open(file, 'w')
    f.write(header + '\n')

    # loop over the rows of the output file
    for i in range(numRows):

        # start is the index of this row's elements in the list
        start = i * entries_per_row

        # Add in the date, the altitude and the color for this row
        f.write(str(longlist[start]) + ',')
        f.write(str(longlist[start + 1]) + ',')
        f.write(str(longlist[start + 2]) + ',')
        f.write(str(longlist[start + 3]) + ',')
        f.write(str(longlist[start + 4]) + '\n')

    # and that's it
    f.close()



# This appends the next entry onto a row: Done in different locations in the code so consolidated here
def extendRows(pedestal, value, dataTypeScale, colorDC, colorInterval, nColors, lon, lat, year, month, day, colors, rows):
    altValue = pedestal + value*dataTypeScale
    colorIndex = int((altValue - colorDC) / colorInterval)
    if colorIndex < 0: colorIndex = 0
    if colorIndex >= nColors: colorIndex = nColors - 1
    rows.extend([lon, lat, datetime(year, month, day), altValue, colors[colorIndex]])


##############################
#
# Configure the vicsort parameters
#
##############################

# get all the filenames into the list all[]
all = [ f for f in listdir(fullpathdir) if isfile(join(fullpathdir,f)) ]

# flux will be just the fluxes_ files
flux = []

# lat[] and lon[] index just as flux[] does
lat = []
lon = []

# rows[] is populated with output CSV values which are eventually written to a file as WWT input
rows = []

# half that spacing
dlat2 = dlat / 2.0
dlon2 = dlon / 2.0

# These values are actually used to size the rectangular blocks
dlatScale = dlat2*latMag
dlonScale = dlon2*lonMag

# Data starts at 1950. This code does one year from 1950 to 2006 based on yearsSkip
outCounter = 0

# bookkeeping
linesSkip = int(yearsSkip * 365.25)
linesGet = int(yearsGet * 365.25)

# This code only gets 1 in every (1 + linesDaySkip) days; typically 1 in 3
linesDaysBlock = 1 + linesDaySkip
readIterations = linesGet / linesDaysBlock

# create a list flux[] of files that begin with 'qualifier' which is 'fluxes'
for a in all:
    b = a.split('_')
    if b[0] == qualifier: flux.append(a)

# determine lat and lon for each flux file
for a in flux:
    b = a.split('_')           # b[1] is the latitude, b[2] is uu.vvv.csv (csv is literally csv)
    c = b[2].split('.')        # c[0] is uu, c[1] is vvv
    lat.append(float(b[1]))
    lon.append(float(c[0]) + float(c[1])/1000.0)

# in passing the files are assumed uniform
# Data line: 1950,01,07,0.0000,0.1806,0.0000,5.262 where last three are precip? evap? flow? 
# Output format is MULTILINESTRING((l l,l l,l l,l l)),--datetime--,--alt0--,--alt1--,--alt2--

# outer loop is over all the flux files
for i in range(len(flux)):

    # open the next input file
    thisFile = open(join(fullpathdir, flux[i]))

    # skip up to the year we care about
    for j in range(linesSkip):
        thisFile.readline()

    # read the number of lines we want (a year or two for example)
    for j in range(readIterations):

        # skip some lines
        for k in range(linesDaySkip): thisFile.readline()
        
        # read a line
        line = thisFile.readline()
        
        # halt if we somehow hit the end of the file
        if line == '': break

        # break this line up into seven values in the a[] list
        a = line.split(',')

        # determine this altitude, guarding for 'nan' data
        value = float(a[dataTypeIndex])
        if isnan(value): value = 0.0

        if drawOnlySignificantData:
            if value > significanceThreshold[dataTypeIndex]:
                extendRows(pedestal, value, dataTypeScale, colorDC, colorInterval, nColors, lon[i], lat[i], int(a[0]), int(a[1]), int(a[2]), colors, rows)
        else:
            extendRows(pedestal, value, dataTypeScale, colorDC, colorInterval, nColors, lon[i], lat[i], int(a[0]), int(a[1]), int(a[2]), colors, rows)

    # show a pulse
    print "  ...did file " + flux[i]
    
    # this is a 'lazy' file write: rows[] accumulates until there are a bunch; or until we run out of input
    # then this code fires off and writes successive output files; generally one or a few

    if len(rows) > 7200000 or i == len(flux)-1:      # divide by five to get actual number of rows

        # create a numerical extension that will sort properly in a directory listing
        if outCounter < 10: sequentialExtension = '0' + str(outCounter)
        else: sequentialExtension = str(outCounter)

        outCounter += 1
        
        outName = fullpathdir + outfileBase + sequentialExtension + '.csv'

        if drawDataAsMarkers:
             WriteCSVFileWithLonLat(outName, rows, "lon,lat,date,alt,color")
        else:
            WriteCSVFileWithGEOMETRY(outName, rows, "GEOMETRY,date,alt,color", dlonScale, dlatScale, geomType)
        
        # clear the rows[] list
        rows = []

        print '..........wrote file ' + str(outCounter)


