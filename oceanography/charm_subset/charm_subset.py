#### This program subsets the harmonized Underway + Flow Cytometry files

import sys
import os
from os import listdir
from os.path import isfile, join

rootdir = "C:\\Users\\fatla_000\\Documents\\"
datadir = "Data\\"
domaindir = "UW Oceanography\\Sophie\\"
path = rootdir + datadir + domaindir
subsetBase = 'subsetTokyo3'
inputBase = 'charmTokyo3'

f = open(path + inputBase + '.csv')

# The charm file pre-FC columns are: day / file / timestamp / lon / lat / temp / salinity / red 
outputHeader = 'day,file,date,lon,lat,temp,salinity,bulk_red,fsc,chl,pe\n'

nRows = 0
totalRows = 4
start = 11
interLineSkip = 1100

for i in range(start):
    f.readline()

while True:
    r = f.readline()
    if r == '': break
    nRows += 1
    if nRows > totalRows: break
    print nRows
    s = r.split(',')
    nSamples = (len(s) - 9)/3
    checkSamples = int(s[8])
    if nSamples != checkSamples:
        print 'we have a problem at row' + str(nRows) + '\n'
        sys.exit()

    g = open(path + subsetBase + '_' + str(nRows) + '.csv', 'w')
    g.write(outputHeader)

    for i in range(nSamples):
        for j in range(8):
            g.write(str(s[j]) + ',')
        pointer = 9 + i*3
        g.write(str(s[pointer]) + ',')
        g.write(str(s[pointer + 1]) + ',')
        g.write(str(s[pointer + 2]) + '\n')

    g.close()

    for i in range(interLineSkip):
        f.readline()

f.close()

print str(nRows - 1) + ' rows writ\n'


