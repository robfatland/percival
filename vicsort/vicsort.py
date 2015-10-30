import numpy as np
import scipy
import sys
import csv
from datetime import datetime
import os
from os import listdir
from os.path import isfile, join

#### This program sorts out some VIC output into files suitable for import into WWT 

################
#
# Generic Methods for file I/O
# 
################

# Write a CSV row to a file from a passed list
def WriteJaggedRowCSV(row, file):
    # row is a list  
    rowLen = len(row)
    for q in range(rowLen - 1):
        file.write(str(row[q]) + ',')    # CSV row
    file.write(str(row[rowLen - 1]))     # last line no comma
    file.write('\n')

# Write a very long list as a sequence of rows in a CSV file: open and shut
def WriteCSVFile(file, longlist, entries_per_row, header):
    numRows = len(longlist) / entries_per_row
    if numRows * entries_per_row != len(longlist):
        print "The long list does not parse evenly into expected entries per row!!!"
        sys.exit(0)
    f = open(file, 'w')
    f.write(header)
    f.write('\n')
    for i in range(numRows):
        start = i * entries_per_row
        end = start + entries_per_row
        WriteJaggedRowCSV(longlist[start:end], f)
    f.close()

# Generate a datetime from just year, month and day (integers)
def convertYMDToDatetime(y, m, d):
    return datetime(y, m, d, 0, 0, 0)


########################
#
# Custom method for file I/O
#
########################

# Write a long list as a sequence of rows to a CSV file: customized for WWT with GEOMETRY / MULTIPOLYGON WKT
def WriteCSVFileWithGEOMETRY(file, longlist, header, lonScale, latScale):
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
        a0 = str(longlist[start] - lonScale)
        a1 = str(longlist[start] + lonScale)
        b0 = str(longlist[start + 1] - latScale)
        b1 = str(longlist[start + 1] + latScale)

        geomEntry = 'MULTIPOLYGON((' + a0 + ' ' + b0 + ',' + a0 + ' ' + b1 + ','
        geomEntry += a1 + ' ' + b1 + ',' + a1 + ' ' + b0 + ',' + a0 + ' ' + b0 + ')),'

        f.write(geomEntry)
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

# select all filenames conforming to fluxes_*
all = [ f for f in listdir(fullpathdir) if isfile(join(fullpathdir,f)) ]
flux = []
lat = []
lon = []
rows = []

# geographic grid spacing
dlat = 0.08
dlon = 0.08

# half that spacing
dlat2 = dlat / 2.0
dlon2 = dlon / 2.0

# modifying factor for artistic license
latMag = 1.5
lonMag = 1.5

dlatScale = dlat2*latMag
dlonScale = dlon2*lonMag

outCounter = 0
yearsSkip = 49
yearsGet = 1
linesSkip = int(yearsSkip * 365.25)
linesGet = int(yearsGet*365.25)
linesDaySkip = 2
linesDaysBlock = 1 + linesDaySkip
readIterations = linesGet / linesDaysBlock

# These values are used to produce interesting altitude/color from data
a3 = 1000.0
a4 = 10000.0
a5 = 10000.0
pedestal = 6000.0
colors = ['red','orange','green','cyan','blue','white']
nColors = len(colors)
colorDC = pedestal
colorScale = 3000.0

# create a list of files that begin with 'qualifier' which is 'fluxes'
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
# set reference dates so we can verify that every subsequent file follows the same rule
# Data line: 1950,01,07,0.0000,0.1806,0.0000,5.262 where last three are precip? evap? flow? 
# Output format is MULTILINESTRING((l l,l l,l l,l l)),--datetime--,--alt0--,--alt1--,--alt2--

for i in range(len(flux)):
    thisFile = open(join(fullpathdir, flux[i]))
    for j in range(linesSkip):
        thisFile.readline()
    for j in range(readIterations):
        for k in range(linesDaySkip): thisFile.readline()
        line = thisFile.readline()
        if line == '': break
        a = line.split(',')
        altValue = pedestal + float(a[3])*a3
        colorIndex = int((altValue - colorDC) / colorScale)
        if colorIndex < 0: colorIndex = 0
        if colorIndex >= nColors: colorIndex = nColors - 1
        rows.extend([lon[i], lat[i], datetime(int(a[0]), int(a[1]), int(a[2])), altValue, colors[colorIndex]])
    print "  ...did file " + flux[i]
    
    if len(rows) > 7200000 or i == len(flux)-1:      # divide by five to get actual number of rows
        if outCounter < 10: extension = '0' + str(outCounter)
        else: extension = str(outCounter)
        outCounter += 1
        outName = fullpathdir + 'out' + extension + '.csv'
        WriteCSVFileWithGEOMETRY(outName, rows, "GEOMETRY,date,alt0,color", dlonScale, dlatScale)
        rows = []
        print '..........wrote file ' + str(outCounter)


