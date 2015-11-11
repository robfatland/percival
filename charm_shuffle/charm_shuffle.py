#### This program shuffles together harmonized Underway + Flow Cytometry files

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
outputBase = 'charmTokyo3'
indexBase = 'index'

# Charm list
charms = []
all = [ f for f in listdir(path) if isfile(join(path,f)) ]
for a in all:
    b = a.split('_')
    if b[0] == charmBase: charms.append(a)
nCharms = len(charms)

# The underway day-file list and the full underway header
udata = []

# index[] is a list of lists: nCharms elements telling how many entries there are in that underway row
index = []

# open the underway file and skip the header
f = open(uFile)
f.readline() # skip header

# load up the underway data-start list udata[]
while True:
    line = f.readline()
    if line == '': break
    l = line.split(',')
    jd = l[5].split('_')
    day = int(jd[1])
    file = int(l[2])
    lat = 0.0 if l[0] == 'NA' else float(l[0])
    lon = 0.0 if l[1] == 'NA' else float(l[1])
    #     day / file / timestamp / lon / lat / temp / salinity / red [ / number-FC triples ]
    udata.append([day, file, l[7].rstrip('\n'), lon, lat, float(l[3]), float(l[4]), float(l[6])])

f.close()
nUnderway = len(udata)
print 'Underway with ' + str(nUnderway) + ' rows\n'

# To make this work we need to open all nCharms input files, open the index file, and create the output file
# The index file is the number of entries per underway row for each of the nCharms input files; sometimes zero
f = open(path + indexBase + '.csv')
g = open(path + outputBase + '.csv', 'w')

# set input[] to be a list of file objects
inputs = []
for file in charms:
    inputs.append(open(path + file))

for i in range(nUnderway):

    a = f.readline()              # next string from the index file
    indexInfo = a.split(',')[8:]  # a list of nCharms strings as we skip the usual first 8 entries
    if len(indexInfo) != nCharms:    # sanity check
        print 'oh my'
        sys.exit()

    # enlightened: linefeed character at end of string does not impede int() type conversion

    # Let's loop over the charm files that might possibly contribute to this row
    for j in range(nCharms):
        if int(indexInfo[j]) > 0:
            r = inputs[j].readline()
            # udata[i] will be extended by a bunch of strings, perhaps with linefeed characters
            udata[i].extend(r.split(',')[8:])
    
    rowLen = len(udata[i])
    sampLen = (rowLen - 8) / 3

    # ok now we change format: I'm going to insert the number of triples in the row after the first 8 entries
    udata[i].insert(8, sampLen)

    # re-calculate rowLen
    rowLen = len(udata[i])
    
    for j in range(rowLen - 1):

        a = str(udata[i][j]).rstrip('\n') + ','
        g.write(a)

    # enlightened: This may be a "zero" row or a full row. 
    # In the former case the last entry is a numerical Zero.
    # In the latter case the last entry is a string; perhaps with a trailing linefeed
    # To avoid having two linefeeds we strip away any trailing linefeed and then add one deliberately.
    # This line of code only runs once per row so it is not expensive in time.
    a = str(udata[i][rowLen - 1]).rstrip('\n') + '\n'
    g.write(a)

    # This is intended to empty out the row that we just finished writing
    #   since the total memory involved could be large > GB
    udata[i] = []
    print '...row ' + str(i) + ' len ' + str(sampLen)


f.close()
g.close()
for i in range(nCharms):
    inputs[i].close()


