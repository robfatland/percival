##################################
#
# This program harmonizes rows from a query results table, specifically data from a row query from
#   MS Level 1.4 data across multiple datasets. This is called the source table. This documentation will...
#     - ...define the structure of the source table
#     - ...describe data consolidation (harmonization) across degenerate rows
#     - ...describe the output table format
#
# There are two types of columns in the source table: A small set of perfunctory columns with pre-determined 
#   header names; and a larger set of columns associated with samples. These latter (sample columns) are grouped 
#   by datasets; so let's start with datasets.
# 
# In BDS a Dataset is a unit of data published by a researcher. It is typically associated with a particular study
#   and this involves collections of water containing Dissolved Organic Matter (DOM). Each unique water source is 
#   a 'carboy' from which multiple samples may be drawn. Samples, then, are the atomic unit of a BDS dataset and
#   they are given unique names within that dataset. 
# 
# In BDS we operate in terms of tables; so Datasets progress upwards in levels by means of tables. In the case
#   of this program the BDS accommodates FTICR-MS (high resolution mass spectrometry) sample data and processes 
#   that to Level 1.4. A scientist then queries this data to produce a set of output rows from source tables
#   at a particular level. Hence the identifier tuple (dataset, table) is sufficient to pinpoint the source of
#   a query results table row. We abbreviate that in this code as 'dt' for 'dataset-table identifier'.
# 
# Since the query could span many datasets the formula (for example) C10H12O3 could be found multiple times in
#   different datasets, producing redundant formula rows with different dt values. This degeneracy is not really
#   helpful for a scientist trying to analyze this table; so this program consolidates those rows into a single 
#   row to remove the degeneracy.  
#  
# Let's dispense with what is described above as the small set of perfunctory columns. There are 17 of these
#   perfunctory values in each row, taken out of order in a more logical sequence:
#     dataset                      -- the dataset identifier for this row (system data; generally not human-useful)
#     table                        -- the table identifier for this row (system data; generally not human-useful)
#     formula                      -- the molecular formula for this row
#     nr_matches                   -- the number of occurrences of samples in this row where this formula-peak was found
#     Fe, S, P, Na, Cl, H, N, O, C -- the number of corresponding atoms found in the formula
#     I                            -- the mean intensity of sample intensities in this row
#     Meas_m/z                     -- mass / charge ratio (and charge is 1; so effectively formula mass in Daltons)
#     mean_mass                    -- calculated mass from the formula (?)
#     Index                        -- I forget what this is at the moment
#
# Of these 17 only 14 are retained in the output table rows. We sideline dataset and table as described below 
#   and ignore the Index column in the output.
# 
# Now we can return to the sample columns that comprise the rest of the query results table. As noted there will
#   be repeated rows for a given formula since that formula will tend to appear in many of the source datasets.
#   In a given input row the valid samples will have numerical values in their corresponding columns. Other 
#   columns will have value 'NaN'. 
# 
# Suppose there are N such repeated rows all with the same molecular formula. To consolidate we simply combine 
#   them into one row with no NaN values.
# 
# The program writes a second output file (which should be JSON but is currently not (kilroy)) which states
#   how many datasets are involved and then proceeds to give the dt ID for both the dataset and the table.
#   This file also provides the number of samples associated with each dataset. Hence this program takes one
#   input file (query results table) and produces two output files: Consolidated query results as a table and
#   a dt listing as text. The original dataset-table sources could if necessary be recovered from this data
#   given this fact: The output column sequence for the output consolidated table is:
# 
#     14 perfunctory columns followed by...
#     Data columns from the  first dt as listed in the second output file followed by...
#     Data columns from the second dt as listed in the second output file followed by... 
#     ...
#     Data columns from the last dt as found in the second output file.
# 
#############################################################

import sys

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
oFile = path + 'rq_consol.csv'
mFile = path + 'rq_consol_metadata.csv'

# open the query result file
f = open(iFile)
h = f.readline()
headers = h.split(',')
nFields = len(headers)
print 'There are', nFields, 'input header columns'
for i in range(nFields): headers[i] = headers[i].rstrip()

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


nOutFields = nFields - len(stdHdrs) + len(stdOutCols)

# I use dt to abbreviate dataset-table, a unique source identifier. 
# The input file header must match the various standard headers (but they can be at any column). 
# The remaining input file column headers are identifiers for samples.
# We do bookkeeping in-flight to make sure those samples can be associated back with their 
#   source datasets primarily through the dtCols[] list of lists. The first index tracks dts, 
#   the second index tracks column indices (samples) for that dt.

# dtID is a list of (Dataset, Table) identifier tuples
dtID = []

# molecular formulas
formulas = []

out = []            # Output is a list of lists; hence the output consolidated flat table
dtCols = []         # list of lists: each giving column values for sample from a unique dt
dtStarts = []       # list of starting columns in the output row for same

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
            if not i in stdIndcs and not line[i].lower() == 'nan':
                thisDtCols.append(i)

        # Now dtCols[] is up to date
        dtCols.append(thisDtCols)

        # Bookkeeping: Track both the number of samples and the output start column index for this dt
        thisStartColumn = len(stdOutCols)
        for i in range(len(dtID) - 1):
            thisStartColumn += len(dtCols[i])
        dtStarts.append(thisStartColumn)


    # Part 2: If this input row's formula is new: Add it

    thisFormula = line[inIndex(formulaString)]
    if not thisFormula in formulas:
        formulas.append(thisFormula)

        # Only in the case of a new formula do we add a new output row (full of zeros)
        thisOutIndex = len(out) - 1
        out.append([0] * nOutFields)

        # if len(out) > 3:
        #     print 'pausing'

        # print 'append out: nOutFields', nOutFields, '; length of new list:', len(out[len(out)-1])
        if len(out[len(out)-1]) != nOutFields:
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
            if oI >= nOutFields:
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

    # diagnose(out, 'pre offense...')


    # Python quiz: Why does the following line insert an extra element in out[][]?
    # out[outRowIndex][startColumn:startColumn + nCols - 1] = [line[i] for i in dtCols[dtIndex]]
    for i in range(len(dtCols[dtIndex])):
        j = dtCols[dtIndex][i]
        out[outRowIndex][startColumn + i] = line[j]

    # diagnose(out, '    post offense...')


# close the input file
f.close()


# diagnose(out, 'C')


print 'At the close we have', len(formulas), 'unique formulas'
print 'outOfRanges =', outOfRanges
print 'outMismatches =', outMismatches

# out[][] now represents our populated new version of the query results table. It needs an adjustment:
#   Go through each output row and accumulate nr_matches as the number of non-zero peak entries
if False:
    skipOver = len(stdOutCols)
    for i in range(len(out)):
        this_row_nr_matches = 0
        for j in range(nOutFields - skipOver):
            if out[i][j + skipOver] > 0:
                this_row_nr_matches += 1
        out[i][stdOutCols.index(nrMatchesString)] = this_row_nr_matches





# kilroy we should also recalculate the I value to make sure that is correct across the entire row, 
#   non-zero values only

# diagnostic comparing against nOutFields
totalOutColumns = len(stdOutCols)
for i in range(len(dtCols)): totalOutColumns += len(dtCols[i])
print nOutFields, 'out fields ~~~~', totalOutColumns, 'columns...'

# Let's write the output file
g = open(oFile, 'w')

# First let's write a header
headerWrites = 0
for ohdr in stdOutCols:
    g.write(ohdr + ',')
    headerWrites += 1


print 'pre data I wrote std headers =', headerWrites

nIDs = len(dtID)

stupidSum = 14

for i in range(nIDs):

    nHdrsThisID = len(dtCols[i])

    stupidSum += nHdrsThisID
    print 'stupid sum is', stupidSum

    stupidSubSum = 0
    for j in range(nHdrsThisID):
        stupidSubSum += 1
        index = dtCols[i][j]
        trailingChar = ','
        if i == nIDs - 1 and j == nHdrsThisID - 1:
            trailingChar = '\n'
        g.write(headers[index] + trailingChar)
        headerWrites += 1

    print 'stupidSubSum came out', stupidSubSum

print '.......post: I have written', headerWrites

# Now write one row per formula
nNulls = 0
for i in range(len(out)):
    for j in range(nOutFields):
        trailingChar = ','
        if j == nOutFields - 1:
            trailingChar = '\n'
        g.write(str(out[i][j]) + trailingChar)

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