##################################
#
# This program harmonizes rows from a query results table, specifically data from a row query from
#   MS Level 1.4 data across multiple datasets. This is called the source table. Here is the program:
#     - define the structure of the source table
#     - describe data consolidation (harmonization) across degenerate rows
#     - describe the output table format
#
# 
# This code is written with no assumption on column order in the source table. 
#
# There are two types of columns in the source table: A small set of
#   perfunctory columns with pre-determined header names; and a larger set of columns associated with samples
#   that are in turn associated with one or more source datasets. A query is used to generate this table; and
#   the query often includes many datasets (with associated tables) in its search space. 
# 
#     The system has any number of Datasets. Each may have relevant "Level 1.4 MS" tables which will be
#       searched in response to a Row Query. The results are rows from any Dataset + Table combinations that
#       match the query criteria, appended in a table. 
#     The first row of this table is headers that belong in two categories. 
#       The first header category is a standard set of headers that are external to the data of interest.
#       The second header category are sample names taken from datasets that have data values of interest. 
#       We proceed to take these two header categories in sequence.
#
#     There are three types of standard headers: 
#       The dataset header is an identifier that applies to the entire row on which it appears.
#       The table header is also an identifier that applies to the entire row on which it appeears.
#       The standard content headers are 15 or so headers that describe the nature of a molecular formula.
# 
#     Before proceeding to the next category of headers let's take a moment to describe what the data are.
#       The remaining headers are as noted sample names taken from datasets. In order to make the table 
#       rectangular a given row will list all samples from all relevant datasets; but for this row all but
#       one of the sample collections will register NaN as the data value. For the sample collection (Dataset)
#       that is relevant to this row the data values are either peak intensities for this molecule or they 
#       are zero if the peak was not found in that sample. 
# 
#     The all-important point then is that the rows are degenerate: The same molecular formula shows up 
#       multiple times. Suppose that five datasets are searched using a row query; and that each contributes
#       to the query result. Then five rows of the query result will correspond to the exact same molecular
#       formula. To make an abbreviated example we suppose that the datasets are called A, B, C, D, E. 
#       These have respectively dataset identifiers A-DS, B-DS, ... and table identifiers A-Tbl, B-Tbl, ... etc
#       Finally the sample names (there are two samples per Dataset) are A1, A2, B1, B2, ... E1, E2.
# 
#     Now let's consider molecular formula C12H26O10. The table rows for this formula might look like this:
#  
#     DS-ID,   Tbl-ID,   A1,   A2,   Formula,  mean_mass,   B1,   B2,   C1,   C2,   D1,   D2,   E1,   E2
#      A-ID,    A-Tbl,    7,    3,  C12H26O10,     330.7,  NaN,  NaN,  NaN,  NaN,  NaN,  NaN,  NaN,  NaN
#      B-ID,    B-Tbl,  NaN,  NaN,  C12H26O10,     330.7,    5,   10,  NaN,  NaN,  NaN,  NaN,  NaN,  NaN
#      C-ID,    C-Tbl,  NaN,  NaN,  C12H26O10,     330.7,  NaN,  NaN,    4,    0,  NaN,  NaN,  NaN,  NaN
#      D-ID,    D-Tbl,  NaN,  NaN,  C12H26O10,     330.7,  NaN,  NaN,  NaN,  NaN,    6,    9,  NaN,  NaN
#      E-ID,    E-Tbl,  NaN,  NaN,  C12H26O10,     330.7,  NaN,  NaN,  NaN,  NaN,  NaN,  NaN,    1,    1
# 
#     Note that all five rows have the same formula; they are degenerate with the NaN values filling in the 
#       space for Dataset/Sample entries that are not referenced in the Dataset ID + Table ID columns. 
#     Note that the C2 entry in data row 3 is 0. This means that this formula did not appear in the analysis of
#       sample C2. 
#     The goal then is to consolidate this set of five rows into a single row as follows: 
#
#       Formula,   mean_mass,  A1, A2, B1, B2, C1, C2, D1, D2, E1, E2
#     C12H26O10,       330.7,   7,  3,  5, 10,  4,  0,  6,  9,  1,  1
# 
#     Now this consolidation of five rows into one gets rid of all the NaN values and some of the other redundancy
#       so that's good; but what is needed is a separate table that tracks the structure of this new table. It 
#       will list out the source Dataset IDs and Table IDs and for each indpendent Dataset + Table combination it
#       records how many entries there are. In our example as key-value pairs (keeping comma-separated value form):
#
#     Number of Dataset-Table pairs, 5
#     Dataset ID 1,                  A-ID
#     Table ID 1,                    A-Tbl
#     Number of Samples 1,           2
#     Dataset ID 1,                  B-ID
#     Table ID 1,                    B-Tbl
#     Number of Samples 2,           2
#     Dataset ID 1,                  C-ID
#     Table ID 1,                    C-Tbl
#     Number of Samples 3,           2
#     Dataset ID 1,                  D-ID
#     Table ID 1,                    D-Tbl
#     Number of Samples 4,           2
#     Dataset ID 1,                  E-ID
#     Table ID 1,                    E-Tbl
#     Number of Samples 5,           2
# 
#     This preserves all of the table ID information without burdening the consolidated table. 
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

rootdir = "C:\\Users\\fatla_000\\Documents\\"
datadir = "Data\\"
domaindir = "BDS\\MS14Consolidate\\"
path = rootdir + datadir + domaindir
iFile = path + 'rowquery.csv'
oFile = path + 'rq_consol.csv'
mFile = path + 'rq_consol_metadata.csv'

# open the underway file and skip the header
f = open(iFile)
h = f.readline()
headers = h.split(',')
nFields = len(headers)
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


# The strategy is to read through the file once. 
# I use dataset-table as a bit of jargon to indicate a unique source. 
# From the header we learn the indices of the various standard headers and by elimination the locations of 
#   the data columns. 
# From the header we intentionally ignore the fact that we can learn how many samples are in the first dataset-table.
# From the first row of data we get our first formula. Some of the columns will have NaN and some will have integer
#   values. The NaN entries tell which samples are not related to this row's ds-tbl entry. 


# DSTable is a tuple (DS, Table) of identifiers
dtID = []

formulas = []

out = []

dtCols = []                     # list of lists: each giving column values for sample from a unique dt
dtStarts = []                   # list of starting columns in the output row for same
nStdOutCols = len(stdOutCols)

nDataLinesRead = 0

def inIndex(s):
    return stdIndcs[stdHdrs.index(s)]

def outIndex(s):
    return stdOutCols.index(s)

while True:

    # read and chop the next line
    l = f.readline()
    if l == "": break
    nDataLinesRead += 1
    line = l.split(',')
    if len(line) != nFields:
        print 'oh dear I fear that this row has the wrong number of entries'
        sys.exit(0)

    # Some line[] fields fall under standard headers. The rest are either data or NaN.
    # Execution is therefore as follows: 
    #   1. If this is a new dataset-table (dt) entry:
    #        Add that tuple to dtID
    #        Append a list of corresponding sample column numbers to dtCols[]
    #        Track the start column in the output for this set of samples
    #   2. If this row contains a new formula: Add it
    #   3. Copy the data in this line in > out

    # Is this a new dataset-table (dt) combination?
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
        thisStartColumn = nStdOutCols
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
        out.append([0] * nFields)
        thisOut = len(out) - 1

        # We can copy all the stdHdr values to this new out[] row; although note that
        #   nr_matches will be overwritten below. (kilroy) A more robust version of this
        #   would be replicated below for not-new-formulas: Make sure that the same procedure
        #   arrives at identical entries: formula, number of carbon, etcetera; all should be 
        #   consistent with this initial write.
        for hdr in stdOutCols:
            out[thisOut][outIndex(hdr)] = line[inIndex(hdr)]

    # Part 3: Copy in the valid data into the proper formula out[] row

    # This index refers to the dt tuple-ID table, i.e. which one we are using on this in > out
    dtIndex = dtID.index((thisDatasetID, thisTableID))

    # This index tells us which output row to write this row's data
    outRowIndex = formulas.index(thisFormula)

    # Overwrite this output row's Zeros with the data from the readline.
    #   dtStarts[dtIndex] is the first out[] column for this dt
    #   len(dtCols[dtIndex]) is the number of good samples in this row (a list of the sample columns for this dt)
    startColumn = dtStarts[dtIndex]
    if startColumn < len(stdOutCols):
        pass

#     for i in range(len(dtCols[dtIndex])):
#         lineIndex = dtCols[dtIndex][i]
#         if lineIndex >= nFields:
#             pass
#         out[outRowIndex][startColumn + i] = line[lineIndex]

    nCols = len(dtCols[dtIndex])
    out[outRowIndex][startColumn:startColumn + nCols - 1] = [line[i] for i in dtCols[dtIndex]]

f.close()

print 'At the close we have', len(formulas), 'unique formulas'

# The last entry should not have a trailing comma...
# The out[][] will have zeros rather than correct std entries

# Go through each output row and accumulate nr_matches as the number of non-zero peak entries
for i in range(len(out)):
    this_row_nr_matches = 0
    skipOver = len(stdOutCols)
    for j in range(nFields - skipOver):
        if out[i][j + skipOver] > 0:
            this_row_nr_matches += 1
    out[i][stdOutCols.index(nrMatchesString)] = this_row_nr_matches

# Let's write the output file
g = open(oFile, 'w')

# First let's write a header
for ohdr in stdOutCols:
    g.write(ohdr + ',')
for i in range(len(dtID)):
    if i < len(dtID) - 1: endPoint = len(dtCols[i])
    else: endPoint = len(dtCols[i])-1
    for j in range(endPoint):
        index = dtCols[i][j]
        g.write(headers[index] + ',')

lastIndex = dtCols[len(dtID)-1][len(dtCols[len(dtID)-1])-1]
g.write(headers[lastIndex].rstrip('\n') + '\n')


# Now let's write one row per formula
for i in range(len(out)):
    for j in range(len(out[i])-1):
        g.write(str(out[i][j]).rstrip('\n') + ',')
    g.write(str(out[i][len(out[i])-1]).rstrip('\n') + '\n')
g.close()

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
