#### This program produces an index matrix: rows are all of the Underway rows and columns are the
####   sequential charm files produced by 'charm': Each being some number of FC triples appended onto
####   those same Underway rows. This is bookkeeping to prepare to shuffle all the charm files together
####   into a single charm file. 

import numpy as np
import sys
import os
from os import listdir
from os.path import isfile, join

rootdir = "C:\\Users\\fatla_000\\Documents\\"
datadir = "Data\\"
domaindir = "UW Oceanography\\Sophie\\"
path = rootdir + datadir + domaindir
uFile = path + 'Tokyo3_sds_complete.csv'
charmBase = 'charm'
indexBase = 'index'

udfColumns = 8

def allZeros(a):
    for i in len(a):
        if a[i] != 0: return False
    return True

# Get a list of all charm files in the folder
all = [ f for f in listdir(path) if isfile(join(path,f)) ]
charms = []
for a in all:
    b = a.split('_')
    if b[0] == charmBase: charms.append(a)

nCharms = len(charms)
print 'I found ' + str(nCharms) + ' charm files; now loading the underway begins.'

# The underway day-file list and the full underway header
udf = []
indexTable = []

# The data row (output; to be compiled)
data = []

# The input row from the currently considered charm file
input = []

# open the underway file and skip the header
f = open(uFile)
f.readline()

# load up the underway lists udf[] and initialize indexTable[]
while True:
    line = f.readline()
    if line == '': break
    l = line.split(',')
    jd = l[5].split('_')
    day = int(jd[1])
    file = int(l[2])
    lat = 0.0 if l[0] == 'NA' else float(l[0])
    lon = 0.0 if l[1] == 'NA' else float(l[1])
    udf.append((day, file))
    indexTable.append([day, file, l[7].rstrip('\n'), lon, lat, float(l[3]), float(l[4]), float(l[6])])

f.close()

print '\n    ok we are underway with ' + str(len(udf)) + 'udf elements\n\n'

nUnderway = len(udf)


print 'The charms are: '
for i in range(nCharms):
    print charms[i]


# Now let's fill in the entire indexTable[][] with Zeros
# This is the presumption of 'no-entry' for each underway-row x charm-file
for i in range(nUnderway):
    for j in range(nCharms):
        indexTable[i].append(0)

# fill in non-zero entries of indexTable[]
for i in range(nCharms):

    print 'starting on charm file ' + charms[i]

    # this file does not have all nUnderway rows
    f = open(path + charms[i])

    nRowsThisFile = 0
    while True:
        r = f.readline()
        if r == "": break
        nRowsThisFile += 1
        s = r.split(',')
        index = udf.index((int(s[0]),int(s[1])))

        # append an entry to indexTable[] equal to how many triples there were in this line of this file
        indexTable[index][i + udfColumns] = (len(s) - udfColumns) / 3
    
    # close that input     
    f.close()

    totalZeroLines = nUnderway - nRowsThisFile
    print '  charm file ' + str(i) + ' has ' + str(totalZeroLines) + ' zero rows\n'

# write the indexTable to a flat file
f = open(path + indexBase + '.csv', 'w')
for i in range(nUnderway):
    for j in range(udfColumns + nCharms - 1):
        a = str(indexTable[i][j]) + ','
        f.write(a)
    a = str(indexTable[i][udfColumns + nCharms - 1]) + '\n'
    f.write(a)

f.close()
