#### This program shuffles together harmonized Underway + Flow Cytometry files

import sys
import os
from os import listdir
from os.path import isfile, join

rootdir = "C:\\Users\\fatla_000\\Documents\\"
datadir = "Data\\"
domaindir = "UW Oceanography\\Sophie\\"
path = rootdir + datadir + domaindir
validateBase = 'validate'
outputBase = 'output'

f = open(path + outputBase + '.csv')
# g = open(path + validateBase + '.csv', 'w')

nRows = 0
while True:
    r = f.readline()
    if r == '': break
    print r
    sys.exit()
    nRows += 1
    print nRows
    # s = r.split(',')
    # g.write(str(nRows) + ',' + str(len(s)) + ',' + str((len(s)-8)/3) + '\n')

f.close()
# g.close()

print str(nRows) + 'rows\n'


