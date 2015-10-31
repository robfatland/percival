import sys
from datetime import datetime
from os import listdir
from os.path import isfile, join

#
# This program sorts out some VIC output into files suitable for import into WWT 
# In WWT you would set Look At = Earth, open the Layer Manager, right click, select Add, open the CSV file...
# From there you'll need to make some adjustments to the imported layer:
#   Select the new layer and click 'Time Series' so it knows it is time-enabled
#   Set the Properties to include a nice time delay value like 8 or 16 days
#   Right-click the layer and set the opacity to very faint to see the underlying terrain
#

########################
#
# Custom method for file I/O (Worldwide Telescope WKT formatting)
#
########################

# Write a long list as a sequence of rows to a CSV file: customized for WWT with GEOMETRY / MULTIPOLYGON WKT
def WriteCSVFileWithGEOMETRY(file, longlist, header, dlonScale, dlatScale):
    # expect header to be GEOMETRY date altitude color for a total of five values
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
        geomEntry = 'MULTIPOLYGON((' + a0 + ' ' + b0 + ',' + a0 + ' ' + b1 + ','
        geomEntry += a1 + ' ' + b1 + ',' + a1 + ' ' + b0 + ',' + a0 + ' ' + b0 + ')),'

        f.write(geomEntry)

        # Add in the date, the altitude and the color for this row
        f.write(str(longlist[start + 2]) + ',')
        f.write(str(longlist[start + 3]) + ',')
        f.write(str(longlist[start + 4]) + '\n')

    # and that's it
    f.close()

##############################
#
# Configure the vicsort parameters
#
##############################


# path information
rootdir = "C:\\Users\\fatla_000\\Documents\\"
datadir = "Data\\"
domaindir = "Jeff Richey Brazil DIF\\"
fullpathdir = rootdir + datadir + domaindir
qualifier = "fluxes"

# get all the filenames into the list all[]
all = [ f for f in listdir(fullpathdir) if isfile(join(fullpathdir,f)) ]

# flux will be just the fluxes_ files
flux = []

# lat[] and lon[] index just as flux[] does
lat = []
lon = []

# rows[] is populated with output CSV values which are eventually written to a file as WWT input
rows = []

# geographic grid spacing: hardcoded to be just under perfect
dlat = 0.08
dlon = 0.08

# half that spacing
dlat2 = dlat / 2.0
dlon2 = dlon / 2.0

# here is a little modifying factor for artistic license
latMag = 1.5
lonMag = 1.5

# These values are actually used to size the rectangular blocks
dlatScale = dlat2*latMag
dlonScale = dlon2*lonMag

# Data starts at 1950. This code does one year from 1950 to 2006 based on yearsSkip
outCounter = 0
yearsSkip = 7

# This code only gets a year or two of data
yearsGet = 1

# bookkeeping
linesSkip = int(yearsSkip * 365.25)
linesGet = int(yearsGet*365.25)

# This code only gets 1 in every (1 + linesDaySkip) days; typically 1 in 3
linesDaySkip = 2
linesDaysBlock = 1 + linesDaySkip
readIterations = linesGet / linesDaysBlock

# The output file retains "when" and "how long" for this data subset
outfileBase = 'vicsort_' + str(1950 + yearsSkip) + '_' + str(yearsGet) + '_'

# These values are used to produce interesting altitude/color from data
# a3 is fourth column in the source: I forget what it is
# a4 is fifth "
# a5 is sixth "
# a6 is seventh "
# Only the a3 constant has been tested
a3 = 1000.0
a4 = 10000.0
a5 = 10000.0
a6 = 10000.0

# place the data on a pedestal to get it up above most of the topography (6000 meters)
pedestal = 6000.0

# the color coding is based on the data column of interest (a3/a4/a5) which becomes altitude
# it *could* be done based on a different column than the altitude at the risk of being confusing
colors = ['red','orange','green','cyan','blue','white']
nColors = len(colors)
colorDC = pedestal
colorScale = 3000.0

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

        # determine this altitude
        altValue = pedestal + float(a[3])*a3

        # determine this color
        colorIndex = int((altValue - colorDC) / colorScale)

        # make sure it doesn't fall outside the possible index range for colors
        if colorIndex < 0: colorIndex = 0
        if colorIndex >= nColors: colorIndex = nColors - 1

        # list.extend() appends several list elements
        rows.extend([lon[i], lat[i], datetime(int(a[0]), int(a[1]), int(a[2])), altValue, colors[colorIndex]])

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
        WriteCSVFileWithGEOMETRY(outName, rows, "GEOMETRY,date,alt0,color", dlonScale, dlatScale)
        
        # clear the rows[] list
        rows = []

        print '..........wrote file ' + str(outCounter)


