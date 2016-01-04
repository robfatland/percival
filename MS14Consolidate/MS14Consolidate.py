##################################
#
# This program harmonizes MS1.4 table data from a row query to consolidate rows with the same 
#   molecular formula.
#
# We begin with a more detailed statement of the problem at hand and include asides on jargon.
#   First it would be ideal to write this with no dependence on column order. The columns of the file
#   need a careful explanation.
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
iodineString = 'I'
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

standardHeaders = [datasetIDString, tableIDString, nrMatchesString, meanMassString, \
    iodineString, ironString, sodiumString, chlorineString, phosphorousString, \
    sulfurString, oxygenString, nitrogenString, hydrogenString, carbonString, \
    formulaString, indexString, measMZString]

# These indices are where the various header strings reside in the standardHeaders[] list             
datasetIDIndex = standardHeaders.index(datasetIDString)
tableIDIndex = standardHeaders.index(tableIDString)
nrMatchesIndex = standardHeaders.index(nrMatchesString)
meanMassIndex = standardHeaders.index(meanMassString)
iIndex = standardHeaders.index(iodineString)
feIndex = standardHeaders.index(ironString)
naIndex = standardHeaders.index(sodiumString)
clIndex = standardHeaders.index(chlorineString)
pIndex = standardHeaders.index(phosphorousString)
sIndex = standardHeaders.index(sulfurString)
oIndex = standardHeaders.index(oxygenString)
nIndex = standardHeaders.index(nitrogenString)
hIndex = standardHeaders.index(hydrogenString)
cIndex = standardHeaders.index(carbonString)
formulaIndex = standardHeaders.index(formulaString)
indexIndex = standardHeaders.index(indexString)
measMZIndex = standardHeaders.index(measMZString)

# standardIndices records the column index in the query results table of the above 'standardized' column names
standardIndices = []

# The list of standard header indices will be in the same order as found above in standardHeaders
for hdr in standardHeaders:
    if hdr in headers:
        thisIndex = headers.index(hdr)
        standardIndices.append(thisIndex)
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

# nDatasetTables is the count of independent sources of row information
nDatasetTables = 0
datasetID = []
tableID = []
nSampleColumns = []

foundFormulas = []
foundNrMatches = []
foundMeanMass = []
foundI = []
foundFe = []
foundNa = []
foundCl = []
foundP = []
foundS = []
foundO = []
foundN = []
foundH = []
foundC = []
foundMeasMZ = []

nDataLinesRead = 0

while True:
    l = f.readline()
    if l == "": break

    nDataLinesRead += 1
    # if nDataLinesRead > 10: break

    line = l.split(',')
    if len(line) != nFields:
        print 'oh dear I fear that baby John has fallen in the jam! and this row has the wrong number of entries'
        sys.exit(0)

    # Let's determine if this row features a dataset-table combination we have not yet seen...
    #   And it is to be expected that this will uncover new formulas throughout the depth of the table
    thisDatasetID = line[standardIndices[datasetIDIndex]]
    thisTableID = line[standardIndices[tableIDIndex]]
    if not (thisDatasetID in datasetID) or not (thisTableID in tableID):
        datasetID.append(thisDatasetID)
        tableID.append(thisTableID)
        nSampleColumns.append(4321)
        nDatasetTables += 1
        print '         OY I FOUND A NEW DATASET-TABLE, total is now', nDatasetTables 

        # Here is where the NaNs versus the numbers could be accumulated...
        thisDSTableColumns = []
        for i in range(nFields):
            if not i in standardIndices:
                pass
                # if is a non-negative number line[i]: thisDSTableColumns.append(i)


    # At this point we have a split in execution path: If this is a new formula then deal with it as such; or else
    #   if this is a known formula then let's assume we have a new Dataset-Table set of entries.

    thisFormula = line[standardIndices[formulaIndex]]

    if thisFormula in foundFormulas:
        # print 'formula', thisFormula, 'is already known'
        pass
    else:
        print 'found new formula =', thisFormula
        foundFormulas.append(thisFormula)

f.close()

print 'At the close we have', len(foundFormulas), 'unique formulas'

g = open(oFile, 'w')
# First let's write a new header
g.write('formula\n')
# Now let's write one row per formula
for i in range(len(foundFormulas)):
    g.write(foundFormulas[i] + '\n')
g.close()

gm = open(mFile, 'w')
gm.write('dataset-tables,')
gm.write(str(nDatasetTables) + '\n')
for i in range(nDatasetTables):
    gm.write('dataset ID-' + str(i) + ',')
    gm.write(datasetID[i] + '\n')
    gm.write('table ID-' + str(i) + ',')
    gm.write(tableID[i] + '\n')
    gm.write('n sample columns-' + str(i) + ',')
    gm.write(str(nSampleColumns[i]) + '\n')
gm.close()
