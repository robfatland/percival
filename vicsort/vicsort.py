import numpy as np
import scipy
import sys
import csv
from datetime import datetime
import os
from os import listdir
from os.path import isfile, join

#### This program sorts out some VIC output into files suitable for import into WWT

# To do: 1999 for four year so skip 365 * 49 rows
# Color
# Eliminate 2 of 3 values in rows to make files smaller
# substitute MULTIPOLYGON
# 

# Write a list to a file based on that list's length: Write as CSV
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

# Write a very long list as a sequence of rows in a CSV file: open and shut but using GEOMETRY / MULTILINESTRING
def WriteCSVFileWithGEOMETRY(file, longlist, entries_per_row, header, dlon, dlat):
    numRows = len(longlist) / entries_per_row
    if numRows * entries_per_row != len(longlist):
        print "The long list does not parse evenly into expected entries per row!!!"
        sys.exit(0)
    f = open(file, 'w')
    f.write(header + '\n')
    for i in range(numRows):
        start = i * entries_per_row
        a0 = str(longlist[start] - dlon2)
        a1 = str(longlist[start] + dlon2)
        b0 = str(longlist[start + 1] - dlat2)
        b1 = str(longlist[start + 1] + dlat2)
        geomEntry = 'MULTILINESTRING((' + a0 + ' ' + b0 + ',' + a0 + ' ' + b1 + ','
        geomEntry += a1 + ' ' + b1 + ',' + a1 + ' ' + b0 + ',' + a0 + ' ' + b0 + ')),'
        f.write(geomEntry)
        f.write(str(longlist[start + 2]) + ',')
        f.write(str(longlist[start + 3]) + ',')
        f.write(str(longlist[start + 4]) + ',')
        f.write(str(longlist[start + 5]) + '\n')
    f.close()

# Generate a datetime from just year, month and day (integers)
def convertYMDToDatetime(y, m, d):
    return datetime(y, m, d, 0, 0, 0)

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

dlat = 0.08
dlon = 0.08
dlat2 = dlat / 2.0
dlon2 = dlon / 2.0
outCounter = 0

a3 = 1000.0
a4 = 10000.0
a5 = 10000.0

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
    while True:
        line = thisFile.readline()
        if line == '': break
        a = line.split(',')
        rows.extend([lon[i], lat[i], datetime(int(a[0]), int(a[1]), int(a[2])), float(a[3])*a3, float(a[4])*a4, float(a[5])*a5])

    print "  ...did file " + flux[i]

    if len(rows) > 7200000:      # divide by six to get actual number of rows: 200k
        if outCounter < 10: extension = '0' + str(outCounter)
        else: extension = str(outCounter)
        outCounter += 1
        outName = fullpathdir + 'out' + extension + '.csv'
        WriteCSVFileWithGEOMETRY(outName, rows, 6, "GEOMETRY,date,alt0,alt1,alt2", dlon, dlat)
        rows = []
        print '..........wrote file ' + str(outCounter)

        if outCounter == 2: sys.exit(0)

# print fluxfiles
# print listdir(fullpathdir2)
print 'kilroy'
a = raw_input()
sys.exit(0)

