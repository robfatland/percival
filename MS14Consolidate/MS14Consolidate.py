##################################
#
# This program harmonizes rows from a query results table, specifically data from a row query from
#   MS Level 1.4 data across multiple datasets. This is called the source table. Here is the program:
#     - define the structure of the source table
#     - describe data consolidation (harmonization) across degenerate rows
#     - describe the output table format
#
# There are two types of columns in the source table: A small set of perfunctory columns with pre-determined 
#   header names; and a larger set of columns associated with samples. These samples are grouped by datasets; 
#   and the datasets are identified by means of both a dataset ID and a table ID within that dataset. The
#   identifer tuple (dataset-ID, table-ID) is abbreviated herein as 'dt' for dataset-table.  
#  
# For a given row of the results table the combination of molecular formula and dt ID are unique. However
#   once a formula shows up once it may reappear in a later row associated with a different dt ID. This is 
#   a replication of the formula row so now let's describe how to consolidate.
# 
# First suppose that a query result brings in results from N datasets, hence N unique dt-IDs. By and large
#   this means there will be N rows with a given molecular formula. In the first such row all entries (columns)
#   with numerical values will be associated with the first dt-ID. The remaining columns will have value 'NaN'.
#   The second row with this formula (second dt-ID) will have numerical values in columns corresponding to 
#   that second dataset; and as before the rest of the entries will be NaN. 
# 
# To consolidate we simply combine all N rows into one row with no NaN values.
# 
# The program writes a second output file (which should be JSON but is currently not (kilroy)) which states
#   how many datasets are involved and then proceeds to give the dt-ID for both the dataset and the table.
#   This file also provides the number of samples associated with each dataset. 
# 
# As a result of this decomposition into two tables the original data can be recovered.
# 
#############################################################

from os import listdir
from os.path import isfile, join
import sys
import numpy as np


####################
# 
# Configure
#
####################

# The path and data are not part of this Visual Studio Project
rootdir = "C:\\Users\\fatla_000\\Documents\\"
datadir = "Data\\"
domaindir = "BDS\\MS14Consolidate\\"
path = rootdir + datadir + domaindir
iFile = path + 'rowquery.csv'
cleanIFile = path + 'rowquery_clean.csv'
oFile = path + 'rq_consol.csv'
mFile = path + 'rq_consol_metadata.csv'

if False:
    f = open(iFile)
    g = open(cleanIFile, 'w')
    rowLens = []
    nRows = 0
    while True:
        x = f.readline()
        if x == "": break
        nRows += 1
        r = x.split(',')
        check1 = len(r)
        for i in range(len(r)): r[i] = r[i].rstrip()
        for i in range(len(r)-1):
            g.write(r[i] + ',')
        g.write(r[len(r)-1] + '\n')
        check2 = len(r)
        if check1 != check2: 
            pass
        rowLens.append(len(r))

    f.close()
    g.close()

    print 'num rows = ', nRows
    print 'length of rowLens = ', len(rowLens)
    print 'first row has length', rowLens[0]
    nDifferentLengths = 0
    for i in range(nRows - 1):
        j = i + 1
        if rowLens[j] != rowLens[0]:
            print 'rowLens[', j, '] = ', rowLens[j]
            nDifferentLengths += 1

    print 'Number of deviations from first row length = ', nDifferentLengths
    print "I honestly don't see what the problem is here."


# open the query result file
f = open(cleanIFile)
h = f.readline()
headers = h.split(',')
nFields = len(headers)
print 'There are', nFields, 'header columns'
for i in range(nFields): headers[i] = headers[i].rstrip()
nFields1 = len(headers)
print 'There are now', nFields1, 'header columns'
if nFields != nFields1:
    print 'oh they do not match, that is very bad'

print '\n\nThe input file has', nFields, 'data fields.\n'

# The following is the start of a (somewhat labored) attempt to track where everything is 'found'
#   in the row query results table...

# We have a set of standardized column names that will be present in all MS 1.4 tables once
datasetIDString = '$DatasetID'
tableIDString = '$TableID'
nrMatchesString = 'nr matches'
meanMassString = 'mean_mass'
intensityString = 'I'
ironString = 'Fe'
sodiumString = 'Na'
chlorineString = 'Cl'
phosphorousString = 'P'
sulfurString = 'S'
oxygenString = 'O'
nitrogenString = 'N'
hydrogenString = 'H'
carbonString = 'C'
formulaString = 'Formula'
indexString = 'Index'
measMZString = 'Meas_m/z'

# These are the input file headers we expect to find at some location in the column sequence
stdHdrs = [datasetIDString, tableIDString, nrMatchesString, meanMassString, \
    intensityString, ironString, sodiumString, chlorineString, phosphorousString, \
    sulfurString, oxygenString, nitrogenString, hydrogenString, carbonString, \
    formulaString, indexString, measMZString]

# These are the column indices of those same standard headers... to be populated below
stdIndcs = []

# These will be the output 'standardized' columns using the same column names as above
stdOutCols = [nrMatchesString, meanMassString, intensityString, ironString, sodiumString, \
    chlorineString, phosphorousString, sulfurString, oxygenString, nitrogenString, hydrogenString, \
    carbonString, formulaString, measMZString]

# The list of standard header indices will be in the same order as found above in stdHdrs
for hdr in stdHdrs:
    if hdr in headers:
        thisIndex = headers.index(hdr)
        stdIndcs.append(thisIndex)
        print 'header', hdr, 'is found in column', thisIndex
    else:
        print 'Header', hdr, 'could not be found in the header list! halting.'
        sys.exit()


# I use dt to abbreviate dataset-table, a unique source identifier. 
# From the header we learn the indices of the various standard headers. The remaining headers are proper names for
#   the samples; and we do the bookkeeping in-flight to make sure those samples can be associated back with their 
#   source datasets.

# dtID is a list of (DS, Table) identifier tuples
dtID = []

# molecular formulas
formulas = []

# Output is a list of lists; each being a unique formula
out = []

dtCols = []                     # list of lists: each giving column values for sample from a unique dt
dtStarts = []                   # list of starting columns in the output row for same

def inIndex(s):
    return stdIndcs[stdHdrs.index(s)]

def outIndex(s):
    return stdOutCols.index(s)

outMismatches = 0
outOfRanges = 0

while True:

    # read and chop the next line
    l = f.readline()
    if l == "": break
    line = l.split(',')
    for i in range(len(line)): line[i] = line[i].rstrip()
    if len(line) != nFields:
        print 'oh dear I fear that this row has the wrong number of entries'













    # Some line[] fields fall under standard headers. The rest are either numerical data or NaN.
    # Execution is therefore as follows: 
    #   1. If this is a new dataset-table (dt) entry:
    #        Add that tuple to dtID
    #        Append a list of corresponding sample column numbers to dtCols[]
    #        Track the start column in the output for this set of samples
    #   2. If this row contains a new formula: Add it
    #   3. Copy the data in this line in > out

    # Part 1. Is this a new dataset-table (dt) combination?
    thisDatasetID = line[inIndex(datasetIDString)]
    thisTableID = line[inIndex(tableIDString)]
    if not (thisDatasetID, thisTableID) in dtID:

        dtID.append((thisDatasetID, thisTableID))

        # Here a list of valid columns are inferred: They have legit non-negative values
        thisDtCols = []                
        for i in range(nFields):

            # Build this list: skip stdHdr columns and avoid NaNs (ignoring case and whitespace)
            if not i in stdIndcs and not line[i].rstrip().lower() == 'nan':
                thisDtCols.append(i)

        # Now dtCols[] is up to date
        dtCols.append(thisDtCols)

        # Bookkeeping: Track both the number of samples and the output start column index for this dt
        thisStartColumn = len(stdOutCols)
        for i in range(len(dtID) - 1):
            thisStartColumn += len(dtCols[i])
        dtStarts.append(thisStartColumn)

        # print '  OY Found', nNans, 'nans,', len(thisDtCols), 'data columns,', \
        #     len(stdIndcs), 'std cols, sum is ', \
        #     nNans + len(thisDtCols) + len(stdIndcs), \
        #     ', compare nFields = ', nFields













    # Part 2: If this input row's formula is new: Add it

    thisFormula = line[inIndex(formulaString)]
    if not thisFormula in formulas:
        formulas.append(thisFormula)

        # Only in the case of a new formula do we add a new output row (full of zeros)
        out.append(['x'] * nFields)
        # print 'append out: nFields', nFields, '; length of new list:', len(out[len(out)-1])
        if len(out[len(out)-1]) != nFields:
            print 'boy that is strange!'
            outMismatches += 1
        thisOut = len(out) - 1

        # We can copy all the stdHdr values to this new out[] row; although note that
        #   nr_matches will be overwritten below. (kilroy) A more robust version of this
        #   would be replicated below for not-new-formulas: Make sure that the same procedure
        #   arrives at identical entries: formula, number of carbon, etcetera; all should be 
        #   consistent with this initial write.
        for hdr in stdOutCols:
            oI = outIndex(hdr)
            if oI >= nFields:
                outOfRanges += 1
            out[thisOut][oI] = line[inIndex(hdr)]











    # Part 3: Copy in the valid data into the proper formula out[] row

    # This index refers to the dt tuple-ID table, i.e. which one we are using on this in > out
    dtIndex = dtID.index((thisDatasetID, thisTableID))

    # This index tells us which output row to write this row's data
    outRowIndex = formulas.index(thisFormula)

    # Overwrite this output row's Zeros with the data from the readline.
    #   dtStarts[dtIndex] is the first out[] column for this dt
    #   len(dtCols[dtIndex]) is the number of good samples in this row (a list of the sample columns for this dt)
    startColumn = dtStarts[dtIndex]

    # This writes the stretch of data from line[] to out[][]
    nCols = len(dtCols[dtIndex])
    out[outRowIndex][startColumn:startColumn + nCols - 1] = [line[i] for i in dtCols[dtIndex]]

# close the input file
f.close()












print 'At the close we have', len(formulas), 'unique formulas'
print 'outOfRanges =', outOfRanges
print 'outMismatches =', outMismatches

# out[][] now represents our populated new version of the query results table. It needs an adjustment:
#   Go through each output row and accumulate nr_matches as the number of non-zero peak entries
if False:
    for i in range(len(out)):
        this_row_nr_matches = 0
        skipOver = len(stdOutCols)
        for j in range(nFields - skipOver):
            if out[i][j + skipOver] > 0:
                this_row_nr_matches += 1
        out[i][stdOutCols.index(nrMatchesString)] = this_row_nr_matches





# kilroy we should also recalculate the I value to make sure that is correct across the entire row, 
#   non-zero values only

# diagnostic comparing against nFields
totalColumns = len(stdHdrs)
for i in range(len(dtCols)):
    totalColumns += len(dtCols[i])
print nFields, 'fields versus', totalColumns, 'columns...'
if nFields != totalColumns:
    print 'nFields', nFields, '; whereas total columns', totalColumns

# Let's write the output file
g = open(oFile, 'w')

# First let's write a header
for ohdr in stdOutCols:
    g.write(ohdr + ',')
headerWrites = len(stdOutCols)
print 'pre writing sample header column names: I have written this many:', headerWrites

nZeroEntries = 0
for i in range(len(dtID)):
    if i < len(dtID) - 1: endPoint = len(dtCols[i])
    else: endPoint = len(dtCols[i])-1
    for j in range(endPoint):
        index = dtCols[i][j]
        if len(headers[index]) == 0:
            g.write('zymurgy,')
            nZeroEntries += 1
        else:
            g.write(headers[index] + ',')

# finish up the header write with a \n
lastIndex = dtCols[len(dtID)-1][len(dtCols[len(dtID)-1])-1]
g.write(headers[lastIndex].rstrip('\n') + '\n')

print 'Number of zero header writes = ', nZeroEntries
print 'Not counting the last header: ', headers[lastIndex]

# Now write one row per formula
nNulls = 0
for i in range(len(out)):
    if len(out[i]) != nFields:
        print 'row',i,'has',len(out[i]),'values; compare nFields =', nFields
    for j in range(len(out[i])-1):
        g.write(str(out[i][j]) + ',')
        if len(str(out[i][j])) < 1:
            print "oops at ij =", i, j
            g.write('zymurgy,')
            nNulls += 1
        else: 
            g.write(str(out[i][j]) + ',')
    if len(out[i][len(out[i])-1]) < 1:
        g.write("zymurgy\n")
    else:
        g.write(str(out[i][len(out[i])-1]) + '\n')

g.close()

# gm is the output metadata file: It describes the source datasets and their samples
gm = open(mFile, 'w')
gm.write('num dts,')
gm.write(str(len(dtID)) + '\n')
for i in range(len(dtID)):
    gm.write('dataset ID-' + str(i) + ',')
    gm.write(dtID[i][0] + '\n')
    gm.write('table ID-' + str(i) + ',')
    gm.write(dtID[i][1] + '\n')
    gm.write('num cols-' + str(i) + ',')
    gm.write(str(len(dtCols[i])) + '\n')
gm.close()