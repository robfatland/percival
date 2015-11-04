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
####   For simplicity we index the big FC file from row 0 = header, 1, 2, ... are data 
####
#### FC rows are appended as decimal-truncated triples to the day-file corresponding Underway rows
####   This means that the rows are jagged and can be quite long.
####
#### While running we write to a progress file called charmInProgress_working.csv. When we are done working on it
####   we rename it charmResult_a_b_c.csv. 
####     a = the last completed row of the FC file numbered from 1, 2, ... (0 is header)
####     b = the row that this file starts on
####     c = the number of properly sorted FC rows, i.e. rows that found Underway bins
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
####   There are no bad data values in U or FC: temp, sal, red, fwd, chlor and pe are all good numbers
####       U values temp sal red are retained as float precision; however to cut output file size:
####       For FC values it is acceptable precision to round to integer values.
####           Dynamic range of FC values is -65k to 65kj
####   5727 rows in the Underway file as contiguous 3-minute intervals implies a cruise of 11.9 days
####       The actual date-time range is 2011-09-19 10:57:00 to 2011-10-02 08:26:00.
####       This is 12 days 21 hours 29 minutes, about one day more than the day-file interval seems to indicate
####       The point is that the Underway record is about 10% gappy and the FC assignment is also a bit gappy.
####

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
# 
# Header and first data row: fsc = forward scatter, chl = chlorophyll, pe = phycoerythrin
#  Cruise,      Day, File_Id,            fsc_adj,             chl_adj,              pe_adj
# Tokyo_3, 2011_263,     136, -19052.87804878049, -10591.439024390245, -26775.975609756097
# 
# It is a 20GB file and about 80 bytes per row so something like 150 million FC rows
#

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
# udf[] is the Underway day-file List: Each element is a tuple. These give us the reference information for
#   binning the FC data; but the FC data is appended to elements of udata[].
# udata[] is a list of lists.  Each list/row of udata begins as the Underway basis row: 8 values.  
#   Each row may subsequently have FC triples appended to it.
#   The rows are re-ordered as follows:
#     day / file / timestamp / lon / lat / temp / salinity / red 
#   The entire Underway dataset is easily held in memory.
#

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
# Cruise                  (ignore)
# Day                     (parse yyyy_doy into just doy)
# File                    (second part of the DF-identifier)
# Forward scatter         (data)
# Chlorophyll             (data)
# Phycoerythrin           (data)
#

####################
# 
# Configure
#
####################

rootdir = "C:\\Users\\fatla_000\\Documents\\"
datadir = "Data\\"
domaindir = "UW Oceanography\\Sophie\\"
path = rootdir + datadir + domaindir
uFile = path + 'Tokyo3_sds_complete.csv'
fcFile = path + 'armbrustlab_seaflow_phyto_adj_tokyo3.csv'
charmBase = 'charm'
histogramFile = path + 'charm_histogram.csv'

numLinesToDo = 40000000
modulusReportOut = 250000

# Let's make tying together all the charm output a later problem
writeOnlyFCAddedRows = True

# retaining all the underway column data in the output
underwayArgsPerLine = 8

# Going to write this as flat as possible (not with triples)
fcNum = 3

# Get a list of all files in the folder
all = [ f for f in listdir(path) if isfile(join(path,f)) ]

# Get a list of all existing charm results files
results = []
for a in all:
    b = a.split('_')
    if b[0] == charmBase: results.append(a)

# set up to answer 'how far have we got so far?'
faveResultsFile = ''
resultsFileExists = True
if len(results) == 0: resultsFileExists = False
maxResultsLines = 0

# how far have we got so far?
if resultsFileExists:
    # We want the prog file with the most lines in it
    for r in results:
        r1 = r.split('_')
        thisLines = int(r1[1])
        if thisLines > maxResultsLines:
            maxResultsLines = thisLines
            faveResultsFile = r1
    print 'my fave results file is ', faveResultsFile
else:
    print 'no results files found.'

fcStartLine = maxResultsLines + 1
print 'I will start on line ', fcStartLine, ' of the FC file'


##########################
#######
####### diagnostics
#######
####### Two aspects:
#######   File self-consistency for both Underway and FC
#######   Harmonization of FC to Underway by means of Day + File abbreviated DF
#######
##########################

# Number of times a FC entry could not be matched to a DF row
numDFFails = 0

# Underway index of first/last row where arg count does not match header
argFailFirstIndexU = -1
argFailLastIndexU = -1

# CF index of first/last row where arg count does not match header
argFailFirstIndexCF = -1
argFailLastIndexCF = -1

# Has the Underway/CF arg count ever failed?
argFailU = False
argFailFC = False

# number of times the Underway/CF arg count does not match header
numArgFailU = 0
numArgFailCF = 0


# The underway day-file list
udf = []

# The underway + appended FC triples list of lists
udata = []

# open the underway file and skip the header
f = open(uFile)
f.readline()

# load up the underway lists udf[] and udata[]
while True:
    line = f.readline()
    if line == '': break
    l = line.split(',')
    if len(l) != underwayArgsPerLine:
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
    # dt = convertStringToDatetime(l[7])
    udf.append((day, file))
    udata.append([day, file, l[7].rstrip('\n'), lon, lat, float(l[3]), float(l[4]), float(l[6])])

f.close()

print '\n    ok we are underway.\n\n'

# set up the FC file; lseek to the first row we want
f = open(fcFile)
for i in range(fcStartLine): f.readline()
counter = 0
nFCExtends = 0
fcArgsPerLine = 6

# read rows from FC; append when possible to udata using udf to determine the index
while True:

    line = f.readline()
    if line == '': break
    counter += 1
    l = line.split(',')

    # some diagnostics on is it going ok?
    #if len(l) != fcArgsPerLine:
    #    numArgFailFC += 1
    #    if not argFailFC:
    #        argFailFC = True
    #        argFailFirstIndexFC = numLinesFC
    #    else:
    #        argFailLastIndexFC = numLinesFC

    # shout out every n'th
    if counter % modulusReportOut == 0: print counter, 'lines processed from FC'

    # julian day splits yyyy_ddd into year and day strings
    # avoiding this split in favor of more direct / faster...
    # jd = l[1].split('_')
    # day is pulled from yyyy_ddd in l[1] and file is pulled from l[2]
    # kilroy this looks dangerous if the day is only 1 or 2 digits
    # l[0] is the cruise ID; we ignore that here
    # day = int(l[1][-3:])
    # file = int(l[2])

    try: 
        hitIndex = udf.index((int(l[1][-3:]), int(l[2])))
    except ValueError:
        numDFFails += 1
    else:
        # you can append a triple tuple or you could extend 3 numbers
        udata[hitIndex].extend((float(l[3][:9]), float(l[4][:9]), float(l[5][:9])))
        nFCExtends += 1

    if counter >= numLinesToDo: break

# At this point we've fallen out of the above while True with some number of appends to udata[]: 
#   Either owing to trying out numLinesToDo rows of FC or ran out of FC data. In either case
#   'counter' will indicate how many input FC rows we looked at. fcStartLine is the first row of
#   fc we began with and nFCAppends is the number of successful appends from FC. Now we can figure
#   out the proper name of the charm file. 
f.close()

charmFile = path + charmBase + '_' + str(fcStartLine + counter - 1) + '_' + str(fcStartLine) + '_' + str(nFCExtends) + '.csv'
f = open(charmFile, 'w')

# Write out the harmonized output file
zeroDF = 0
nonzeroDF = 0
for i in range(len(udf)):
    if len(udata[i]) > underwayArgsPerLine:
        nonzeroDF += 1
        if writeOnlyFCAddedRows:
            # Write all of the elements of the row separated by commas...
            rowLen = len(udata[i])
            # For rowlen = 10 this loop goes 0, 1, 2, ..., 8
            for q in range(rowLen - 1):
                f.write(str(udata[i][q]) + ',')
            # ...and then we write element 9 with linefeed
            f.write(str(udata[i][rowLen - 1]) + '\n')
    else: 
        zeroDF += 1
        if not writeOnlyFCAddedRows:
            # Diagnostic just writes the lines as str(List)
            f.write(str(udata[i]))
            f.write('\n')

f.close()

## histogram has 100 bins for 'thousands of points'
#histogram = []
#for i in range(100):
#    histogram.append(0)

#for i in range(len(udf)):
#    bin = udata[i][8]/1000
#    histogram[bin] += 1

#for i in range(100):
#    fHistogram.write(str(i*1000))
#    fHistogram.write(',')
#    fHistogram.write(str(histogram[i]))
#    fHistogram.write('\n')
                      
#fHistogram.close() 




##################
#####
##### What happened...
#####
##### All the post-run diagnostics are printed in this block
#####
##################



#print '\n'
#print numLinesU, 'lines of data in Underway; arg count fail =', argFailU
#if argFailU:
#    print 'Underway first arg fail line =', argFailFirstIndexU
#    print 'Underway last arg fail line =', argFailLastIndexU
#    print 'Underway number of arg fails =', numArgFailU
#print '\n'
#print 'The datetime range in Underway is ', udata[0][2], 'to', udata[numLinesU-1][2]
## print 'The interval is ', datetime.timedelta(datetime.datetime(udata[0][2]), datetime.datetime(udata[numLinesU-1][2]))
#print '\n'
#print 'day-file assignment fails = ', numDFFails, 'of attempts = ', numLinesFC
#print '\n'
#print 'min non-zero appends = ', minDFFC, 'and max non-zero appends = ', maxDFFC
#print '\n'
#print 'The last date-file pair in Underway is ', udf[numLinesU - 1][0], '--', udf[numLinesU - 1][1]
#print 'The last date-file reached in the FC scan is ', maxDay, '--', maxFile
#print '\n'


#print 'expect', numLinesU, 'lines; totting up zero-appends and appends gives', zeroDF + nonzeroDF
#print 'zero appends = ', zeroDF, 'and nonzero appends = ', nonzeroDF



# print numLinesB, 'lines of data in flow cytometry (at least)'
# print 'arg count fail =', argFailB
# if argFailB:
#     print 'first fail line =', argFailFirstIndexB
#     print 'last fail line =', argFailLastIndexB
#     print 'number of fails =', numArgFailB

print '\nI think I am done.\n'