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
outputBase = 'output'
indexBase = 'index'


# Charm list
charms = []
all = [ f for f in listdir(path) if isfile(join(path,f)) ]
for a in all:
    b = a.split('_')
    if b[0] == charmBase: charms.append(a)
nCharms = len(charms)

# The underway day-file list and the full underway header
udf = []
udata = []

# The data row (output; to be compiled)
data = []

# index[] is a list of lists: nCharms elements telling how many entries there are in that underway row
index = []

# open the underway file and skip the header
f = open(uFile)
f.readline() # skip header

# load up the underway lists udf[] and udata[]
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
    udata.append([day, file, l[7].rstrip('\n'), lon, lat, float(l[3]), float(l[4]), float(l[6])])

f.close()
nUnderway = len(udf)
print 'Underway with ' + str(nUnderway) + ' rows\n'

# To make this work we need to open all nCharms input files, open the index file, and creat the output file
# The index file is the number of entries per underway row for each of the nCharms input files; sometimes zero
f = open(path + indexBase + '.csv')

g = open(path + outputBase + '.csv', 'w')

# set input[] to be a list of file objects
inputs = []
for file in charms:
    inputs.append(open(path + file))

for i in range(nUnderway):
    print '...row ' + str(i) + ' of total rows = ' + str(nUnderway)

    line = f.readline()              # next string from the index file
    indexInfo = line.split(',')[8:]  # a list of nCharms strings as we skip the usual first 8 entries
    if len(indexInfo) != nCharms:    # sanity check
        print 'oh my'
        sys.exit()
    # enlightened: linefeed character at end of string does not impede int() type conversion
    for j in range(nCharms):
        indexInfo[j] = int(indexInfo[j])     # type convert to integers

    # Let's loop over the charm files that might possibly contribute to this row
    for j in range(nCharms):
        if indexInfo[j] > 0:
            r = input[j].readline()
            s = r.split(',')             # s is a list of strings with the unfortunate \n at the end of the last one maybe
            udata[i].extend(r.split(',')[8:])
    
    rowLen = len(udata[i])
    sampLen = (rowLen - 8) / 3

    # ok now we change format: I'm going to pre-pend the number of triples in the row after the first 8 entries
    udata.insert(8, sampLen)
    rowLen += 1
    
    for j in range(rowLen - 1):
        g.write(str(udata[i][j]) + ',')
    # ...with a trailing linefeed
    g.write(str(udata[i][rowLen - 1]) + '\n')

    # This is intended to empty out the row that we just finished writing
    udata[i] = []

f.close()
g.close()
for i in range(nCharms):
    input[i].close()


