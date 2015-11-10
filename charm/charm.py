##################################
#
# This program harmonizes Flow Cytometry data (O(GB)) to a corresponding Underway file (O(MB))
#
# We begin with a more detailed statement of the problem at hand and include asides on jargon.
# 
# The Flow Cytometry (FC) file is flat: A header row followed by some number of fixed-length data
#   rows where the data are separated by commas. The file format is consequently called CSV for
#   'comma separated values'. The Underway file follows the same convention but of course with 
#   a different header. 
# 
# Jargon: 'Day-file' is jargon here. It refers to a pair of numbers, a tuple, that corresponds to a
#   three minute time window. Many but not all such windows over the course of the research cruise
#   form the 'buckets' into which the time-series data are sorted. Multiple FC values (O(10k)) will
#   be sorted into most of the day-file bins. For a 12 days cruise we have about 5700 day-file bins
#   in the working case that resulted in this code.
#
# The motivation for this program is the idea that associating day-file FC values sorts them in
#   time. As long as we are doing that we might as well also associate the Underway values with 
#   them. In the formative case there are three FC data values (fsc for forward scatter, chl for
#   chlorophyll, and pe for phycoerythrin) which again occur in a typical day-file bin tens of 
#   thousands of times. The Underway file has temperature, salinity and "bulk red" data values;
#   but only such triple associated with each day-time bin. 
# 
# This code was originally written to run piecemeal to reduce the in-memory load on the computer.
#
#                              <<<<IMPORTANT NOTE ON METHOD>>>>>
#
#   The easiest way to simplify this code would be to sort the FC source file by chronological time which
#     MUST correspond to day-file order, e.g. day 100 file 10 NEVER occurs earlier in actual time than
#     day 100 file 8, to use an illustrative example. If this was the case the program could read a set
#     of consecutive FC rows with the same day-file tag, append the resulting row to output, and move on
#     in the input file; no back-tracking in the input file and no need to use 30GB of RAM.
#
#                              <<<<IMPORTANT NOTE ON METHOD>>>>>
#
#   Here is an outline of the steps:
#
# 1. Read the Underway file into two lists: udf[] and udata[]. The former is used for index
#    determination using tuples and the latter is the entire Underway data row. 
# 2. Loop over some desired number of files. For each:
#        - Loop over FC rows, sorting them as 'extend()' into the udata[] rows.
#            . in passing accumulate an index of temp files and Underway rows: Number of FC triples.
#        - Then write that partial-result file
# 3. Start over with the Underway rows loop: Accumulate one row from all the temporary files
#        - Once a single combined row is accumulated it is written to the harmonized output file
#
# Consequences of harmonization: 
#   There will be some FC rows that can not be found in Underway: Discarded
#   Harmonized rows have different lengths depending on how many FC triples were found
#   Some Underway rows receive Zero FC triples
#   All Underway rows have some bookkeeping values appended to the original 8 fields (see below)
#
# After the above harmonizing step: We can proceed to operate on each row independently in
#   terms of data reduction ideas like clustering; and we can proceed with some data cleaning 
#   on the metadata, for example interpolating lat/lon values over segments where that data 
#   drops out between good fixes.
# 
# The other post-harmonizing step to bear in mind is that we can visualize these data in a 
#   variety of ways, for example on Worldwide Telescope (WWT). The 'easy' way to do this is to create
#   a CSV file with headers and format oriented towards the WWT interface since it works well with
#   flat tables.
#  
# Intermediate result files are called charm_a_b_c.csv 
#     a = the last completed row of the FC file numbered from 1, 2, ... (0 is header)
#     b = the row that this file starts on
#     c = the number of properly sorted FC rows, i.e. rows that found Underway bins
# Assumptions etc that this program may not check
#    Day-File values in Underway are unique
#    Cruise column in the FC file does not vary
#    Day-File values in Underway do not need to be resorted chronologically
#    lat / lon == 'NA' values are converted to 0.0 in Underway rows
#      This indiscriminately puts that row at null island
#    There is no datetime ambiguity: Everything is Zulu
#    There are no bad data values in U or FC: temp, sal, red, fwd, chlor and pe are all good numbers (false (kilroy))
#    Dynamic range of FC values is -65k to 65k
#    File format is fixed per the Tokyo3 motivating example.
#
# Details from the motivating Tokyo-3 cruise:   
#   5727 rows in the Underway file (totals 11.9 days but they are not contiguous)
#   Actual Underway date-time range is 2011-09-19 10:57:00 to 2011-10-02 08:26:00.
#     This is 12 days 21 hours 29 minutes
#     Therefore the Underway record is about 10% gappy
#     FC assignment misses about 300 rows entirely; so also gappy
#
#   Underway file: 1 header row + 5727 data rows of data (each row a 3-minute window)
#     Header and first data row. Notice 'day' is in fact year_day so in the case of the first
#     line day-file = (262, 45).
#
#     LAT, LON, file,       OCEAN.TEMP,         SALINITY,      day, BULK.RED,             timestamp
#      NA,  NA,   45, 27.2468196969697, 33.4421954545454, 2011_262, 102.8189, 9/19/2011 10:57:00 PM
# 
#   FC file header and first data row: fsc = forward scatter, chl = chlorophyll, pe = phycoerythrin
#     Cruise,       Day, File_Id,            fsc_adj,             chl_adj,              pe_adj
#     Tokyo_3, 2011_263,     136, -19052.87804878049, -10591.439024390245, -26775.975609756097
# 
#  The FC source file is 20GB and about 284 million rows; of which about 1% are discarded as not
#    matching an Underway day-file. 
# 
# Underway columns:  
#   LAT
#   LON
#   File
#   Temp
#   Salinity
#   Day
#   Bulk.red
#   timestamp
#
# FC columns:
#   Cruise
#   Day
#   File
#   Forward scatter
#   Chlorophyll
#   Phycoerythrin
#
# udf[] is the Underway day-file List: Each element is a tuple providing indices for the FC data.
# udata[] is a list of lists.  Each list/row of udata[] begins as the Underway row: 8 values.  
#   Each row may subsequently have FC triples appended to it.
#
# On file-write the udata[] Underway values are re-ordered more sensibly although this is in fact
#   quite unnecessary since it is not used (kilroy):
#     day / file / timestamp / lon / lat / temp / salinity / red 
#   The entire Underway dataset is easily held in memory.
#
# Python note: How day-file indexing is done once udf[] is populated with (day, file) tuples:
#   dfTuple = (263, 80)
#   if dfTuple in udf: 
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
#############################################################

from os import listdir
from os.path import isfile, join


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
modulusReportOut = 1000000

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

