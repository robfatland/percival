from os import listdir
from os.path import isfile, join

rootdir = ".\\"
datadir = "..\data\\"
domaindir = ".\\"
path = rootdir + datadir + domaindir
csvFile = path + 'T0007.CSV'
outputFile = path + 'T0007_redux.csv'
numLinesToDo = 100000
modulusReportOut = 1000

# open the underway file and skip the header
f = open(csvFile)
for i in range(16):
    f.readline()

g = open(outputFile, 'w')

# load up the underway lists udf[] and udata[]
nLines = 0
nGoodLines = 0
nWriteLines = 0
while True:
    try:
        line = f.readline()
    except: 
        print 'error on line ', nLines

    nLines += 1

    if nLines > 200000: break

    l = line.split(',')

    if len(l) == 3:
        nGoodLines += 1
        # we are (we hope) ok
        if nGoodLines % modulusReportOut == 0:
            g.write(line)
            nWriteLines += 1
            print 'lines: read', nLines, '; good', nGoodLines, '; wrote', nWriteLines 

f.close()
g.close()


    # jd = l[5].split('_')
    # day = int(jd[1])
    # file = int(l[2])
    # lat = 0.0 if l[0] == 'NA' else float(l[0])
    # lon = 0.0 if l[1] == 'NA' else float(l[1])
    # dt = convertStringToDatetime(l[7])
    # udf.append((day, file))
    # udata.append([day, file, l[7].rstrip('\n'), lon, lat, float(l[3]), float(l[4]), float(l[6])])


