#### This program shuffles together harmonized Underway + Flow Cytometry files

import os
from os import listdir
from os.path import isfile, join

#   5727 rows in the charm files (at most!)
#
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
charmBase = 'charm'
shuffleBase = 'shuffle.csv'

# Get a list of all files in the folder
all = [ f for f in listdir(path) if isfile(join(path,f)) ]

# Get a list of all existing charm results files
charms = []
for a in all:
    b = a.split('_')
    if b[0] == charmBase: charms.append(a)

# The underway day-file list and the full underway header
udf = []
udata = []

# The data row (output; to be compiled)
data = []

# The input row from the currently considered charm file
input = []

# open the underway file and skip the header
f = open(uFile)
f.readline()

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

print '\n    ok we are underway.\n\n'

# The output file
f = open(path + shuffleBase, 'w')

input = []
for file in charms:
    input.append(open(path + file))

# now input[] is a bunch of open files
#for i in range(len(udf)):
#    for j in range(len(input)):



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