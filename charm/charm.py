#### This program harmonizes the Flow Cytometry file (20GB) to the Underway file (.5MB)

import matplotlib
from matplotlib import pyplot

import numpy as np
import scipy
import sys
import csv
from datetime import datetime

import os
from os import listdir
from os.path import isfile, join

####
####
#### This program harmonizes the Flow Cytometry file (20GB) to the Underway file (.5MB)
####
#### Jargon: Day-file is a native (tuple!) classification scheme used by both FC and Underway data files.
####   The good news is that they are present in both; so FC rows can be binned into Underway rows.
####   The bad news is that it is unclear if they are unique; so that gets our first kilroy.
####
#### We want this program to run piecemeal because it would otherwise be a bit too memory intensive.
#### Considerations:
####   Does a prior results file exist? If so it should contain the number of FC rows processed
####   How many FC rows find no home underway row?
####   How many underway rows find no FC data? Negligible FC data? 
####
#### FC rows are appended as decimal-truncated triples to the day-file corresponding Underway rows
####   This means that the rows are jagged and can be quite long. 
####
#### Kilroy: Here are assumptions and things this program does not check
####   Assume the Day-File pairs in Underway are unique
####   Assume the value in the Cruise column in the FC file does not vary
####   Assume Day-File pairs are strictly increasing in time in the way that hour-minute pairs are strictly increasing
####   It is acceptable to write the variable-length output rows as comma-separated with the FC triples also comma-separated in parens
####   By default only write Day-File rows from Underway where FC values have been appended
####       This can be turned off but the "Every Underway Row" output is not carefully formatted as CSV; it is just a List print
####   It is ok to change lat / lon == 'NA' values to 0.0 in Underway rows.
####       Note that this indiscriminately puts that row at null island or on the equator or the prime meridian! 
####   There is no datetime ambiguity: Everything is Zulu
####   There are no bad data values in U or FC: temp, sal, red, fwd, chlor and phyc are all good numbers
####       U values temp sal red are retained as float precision; however to cut output file size:
####       For FC values it is acceptable precision to round to integer values.
####           Dynamic range of FC values is -65k to 65kj
####   5727 rows in the Underway file as contiguous 3-minute intervals implies a cruise of 11.9 days
####       The actual date-time range is 2011-09-19 10:57:00 to 2011-10-02 08:26:00.
####       This is 12 days 21 hours 29 minutes, about one day more than the day-file interval seems to indicate
####       The point is that the Underway record is about 10% gappy and the FC assignment is also a bit gappy.
####

rootdir = "C:\\Users\\fatla_000\\Documents\\"
datadir = "Data\\"
domaindir = "UW Oceanography\\Sophie\\"
path = rootdir + datadir + domaindir
underwayFile = path + 'Tokyo3_sds_complete.csv'
flowcyFile = path + 'armbrustlab_seaflow_phyto_adj_tokyo3.csv'
progLabel = 'charmInProgress'
progressBase = path + progLabel + '_'
charmFile = path + 'charm.csv'
histogramFile = path + 'charm_histogram.csv'


# Get a list of all files in the folder
all = [ f for f in listdir(path) if isfile(join(path,f)) ]

# Get a list of all existing progress files
prog = []
for a in all:
    b = a.split('_')
    if b[0] == progLabel: prog.append(a)

progressFileExists = True
if len(prog) == 0: progressFileExists = False

if progressFileExists:
    # We want the prog file with the most lines in it
    maxProgLines = -1
    for p in prog:
        p1 = p.split('_')
        thisLines = int(p1[1])
        if thisLines > maxProgLines:
            maxProgLines = thisLines
            faveProgFile = p1
    print 'my fave progress file is ', p1
else:
    print 'no progress file found.'

# Prep info on Underway file: The one I'm using is 1 header + 5727 rows of data, each a 3 minute window
# Header and first data row:
#   LAT, LON, file,       OCEAN.TEMP,         SALINITY,      day, BULK.RED,             timestamp
#    NA,  NA,   45, 27.2468196969697, 33.4421954545454, 2011_262, 102.8189, 9/19/2011 10:57:00 PM
#
# This code counts the lines in the file:
# fU = open(underwayFile)
# underwayLines = 0
# while True:
#     a = fU.readline()
#     if a == "": break
#     underwayLines += 1
# fU.close()
# print 'counted ', underwayLines, ' lines in the underway file'


# Header and first data row: fsc = forward scatter, chl = chlorophyll, pe = phycoerythrin
#  Cruise,      Day, File_Id,            fsc_adj,             chl_adj,              pe_adj
# Tokyo_3, 2011_263,     136, -19052.87804878049, -10591.439024390245, -26775.975609756097
# 
# It is a 20GB file and about 80 bytes per row so something like 150 million FC rows
#
fFC = open(flowcyFile)
fcLines = 2
a = fFC.readline()
print a
a = fFC.readline()
print a
while True:
    a = fFC.readline()
    if a == "": break
    fcLines += 1
    if fcLines%100000 == 0: print fcLines
fFC.close()
print 'counted ', fcLines, ' lines in the underway file'
sys.exit(0)


##########################
#######
####### diagnostics
#######
####### Two aspects:
#######   File self-consistency for both Underway and FC
#######   Harmonization of FC to Underway by means of Day + File abbreviated DF
#######
##########################

# Track max and min counts for date-file rows assuming they have a non-zero count of FC tuples
minDFFC = 50000000     # A suitably impossibly large number
maxDFFC = 0

# count how many DF rows have tuples, how many don't
zeroDF = 0
nonzeroDF = 0

# Number of times a FC entry could not be matched to a DF row
numDFFails = 0

# keep track of how far along the FC data got in terms of day-file sequence (found only)
maxDay = 0
maxFile = 0

# Underway index of first/last row where arg count does not match header
argFailFirstIndexU = -1
argFailLastIndexU = -1

# number of times the Underway arg count does not match header
numArgFailU = 0

# CF index of first/last row where arg count does not match header
argFailFirstIndexCF = -1
argFailLastIndexCF = -1

# Has the Underway/CF arg count ever failed?
argFailU = False
argFailFC = False

# number of times the Underway/CF arg count does not match header
numArgFailU = 0
numArgFailCF = 0

# How many lines of CF to skip at the top
lineSkipCF = 0

# How many lines of CF to try and process
upperLineCountLimitFC = 500000000

# How often to print stdout the progress of CF processing
modulusReportOut = 500000

# Write out everything or just Underway rows where FC triples have been appended?
writeOnlyFCAddedRows = True

# Open the files
fU = open(fullpathdir + underwayFile)
fFC = open(fullpathdir + flowcyFile)
fHarm = open(fullpathdir + harmFile, 'w')
fHistogram = open(fullpathdir + histogramFile, 'w')





# Parse the Underway header
hdr = fU.readline()
hU = hdr.split(',')
argPerLineU = len(hU)

# Parse the FC header
hdr = fFC.readline()
hFC = hdr.split(',')
argPerLineFC = len(hFC)

# Rows of data per file (not counting header)
numLinesU = 0
numLinesFC = 0
numLinesHarm = 0

a = range(0,10)
b = range(0,10)
pyplot.plot([1,2,3,4])
pyplot.show()
print 'well that was easy; here is a:'
print a
print b




# Disabled header printouts:
#
# for c in range(len(ha)):
#     print 'Underway header', c, 'is:', ha[c]
#
# for c in range(len(hb)):
#    print 'Flow Cytometer header', c, 'is:', hb[c]
#
# Here are the columns for Underway: 
# LAT
# LON
# File
# Temp
# Salinity
# Day
# Bulk.red
# timestamp
#
# Here are the columns for FC
# Cruise
# Day
# File
# Forward scatter
# Chlorophyll
# Phycoerythrin

#
# udf[] is the Underway day-file list (as 2-tuples). These are for looking up where a particular FC row should go.
# 
# udata[] is a copy of the Underway row: A list of 8 values (column indices 0 -- 7) plus a counter N initially set to 0. 
#   Each row may subsequently have FC triples appended to it.
#   Each appended triple will increment the counter in column index = 8
#   Here is the order of the U row columns:
#     day / file / timestamp / lon / lat / temp / salinity / red / N = 0
#   Note that the entire Underway dataset is easily held in program memory. It is when the FC triples start to 
#     accumulate that we could potentially run into memory problems. (This laptop has 32GB RAM.)
#
udf = []
udata = []

while True:
    line = fU.readline()
    if line == '': break
    numLinesU += 1
    l = line.split(',')
    if len(l) != argPerLineU:
        numArgFailU += 1
        if not argFailU:
            argFailU = True
            argFailFirstIndexU = numLinesU
        else:
            argFailLastIndexU = numLinesU
    jd = l[5].split('_')
    day = int(jd[1])
    file = int(l[2])
    lat = 0.0 if l[0] == 'NA' else float(l[0])
    lon = 0.0 if l[1] == 'NA' else float(l[1])
    dt = convertStringToDatetime(l[7])
    udf.append((day, file))
    udata.append([day, file, dt, lon, lat, float(l[3]), float(l[4]), float(l[6]), 0])


#
# Examples of how to verify my python List/Tuple syntax is correct...
#
# print 'udf[100] =', udf[100]
# print 'udf[100][0] = ', udf[100][0]
# print 'udf[100][1] = ', udf[100][1]
# gives us 263 and 80
#
# dfTuple = (263, 80)
# if dfTuple in udf: 
#     hitIndex = udf.index(dfTuple)
#     print udf[hitIndex], ' -- ', udata[hitIndex]
# else:
#     print 'No dfTuple as such in udf'
#



# FC is flow cytometry row information as a List of 6 values in this column order:
#
# Cruise
# Day
# File
# Forward scatter
# Chlorophyll
# Phycoerythrin
#
# Cruise value is ignored

# counter = 0
while True:
    line = fFC.readline()
    #counter += 1
    #if counter % modulusReportOut == 0: 
    #    print counter, 'lines of FC file processed,', numLinesFC, 'ingested to Underway'

    #if counter > lineSkipCF:
    if line == '': break
    numLinesFC += 1
    l = line.split(',')
    if len(l) != argPerLineFC:
        numArgFailFC += 1
        if not argFailFC:
            argFailFC = True
            argFailFirstIndexFC = numLinesFC
        else:
            argFailLastIndexFC = numLinesFC
    if numLinesFC > upperLineCountLimitFC: break
    if numLinesFC % modulusReportOut == 0: 
        print numLinesFC, 'lines of FC file processed'
    jd = l[1].split('_')
    day = int(jd[1])
    file = int(l[2])
    dfTuple = (day, file)
    if dfTuple in udf: 
        hitIndex = udf.index(dfTuple)
        udata[hitIndex][8] += 1

        # Track the furthest along in time (day-file) a matched FC gets
        if (day == maxDay and file > maxFile) or (day > maxDay):
            maxDay = day
            maxFile = file

        # Here we try to track the minimum and maximum number of FC triples added to an Underway row
        if udata[hitIndex][8] < minDFFC: minDFFC = udata[hitIndex][8]
        if udata[hitIndex][8] > maxDFFC: maxDFFC = udata[hitIndex][8]

        # Append the FC triple to the Underway row identified as having the same day-file pair
        # Note that FC columns 0, 1, and 2 do not make an appearance; just the fwd/chlor/phy triple
        udata[hitIndex].append((int(float(l[3])), int(float(l[4])), int(float(l[5]))))
    else:
        numDFFails += 1

# Write out the harmonized output file
for i in range(len(udf)):
    if udata[i][8] > 0:
        nonzeroDF += 1
        if writeOnlyFCAddedRows:
            # Write all of the elements of the row separated by commas...
            rowLen = len(udata[i])
            # For rowlen = 10 this loop goes 0, 1, 2, ..., 8
            for q in range(rowLen - 1):
                fHarm.write(str(udata[i][q]) + ',')
            # ...and then we write element 9 with no following comma...
            fHarm.write(str(udata[i][rowLen - 1]))
            # ...and then a line return
            fHarm.write('\n')
    else: 
        zeroDF += 1
        if not writeOnlyFCAddedRows:
            # Diagnostic just writes the lines as str(List)
            fHarm.write(str(udata[i]))
            fHarm.write('\n')

fHarm.close()

# histogram has 100 bins for 'thousands of points'
histogram = []
for i in range(100):
    histogram.append(0)

for i in range(len(udf)):
    bin = udata[i][8]/1000
    histogram[bin] += 1

for i in range(100):
    fHistogram.write(str(i*1000))
    fHistogram.write(',')
    fHistogram.write(str(histogram[i]))
    fHistogram.write('\n')
                      
fHistogram.close() 




##################
#####
##### What happened...
#####
##### All the post-run diagnostics are printed in this block
#####
##################



print '\n'
print numLinesU, 'lines of data in Underway; arg count fail =', argFailU
if argFailU:
    print 'Underway first arg fail line =', argFailFirstIndexU
    print 'Underway last arg fail line =', argFailLastIndexU
    print 'Underway number of arg fails =', numArgFailU
print '\n'
print 'The datetime range in Underway is ', udata[0][2], 'to', udata[numLinesU-1][2]
# print 'The interval is ', datetime.timedelta(datetime.datetime(udata[0][2]), datetime.datetime(udata[numLinesU-1][2]))
print '\n'
print 'day-file assignment fails = ', numDFFails, 'of attempts = ', numLinesFC
print '\n'
print 'min non-zero appends = ', minDFFC, 'and max non-zero appends = ', maxDFFC
print '\n'
print 'The last date-file pair in Underway is ', udf[numLinesU - 1][0], '--', udf[numLinesU - 1][1]
print 'The last date-file reached in the FC scan is ', maxDay, '--', maxFile
print '\n'


print 'expect', numLinesU, 'lines; totting up zero-appends and appends gives', zeroDF + nonzeroDF
print 'zero appends = ', zeroDF, 'and nonzero appends = ', nonzeroDF



# print numLinesB, 'lines of data in flow cytometry (at least)'
# print 'arg count fail =', argFailB
# if argFailB:
#     print 'first fail line =', argFailFirstIndexB
#     print 'last fail line =', argFailLastIndexB
#     print 'number of fails =', numArgFailB

print '\nI think I am done.\n'