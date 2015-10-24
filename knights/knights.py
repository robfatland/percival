# Start with skeleton code

class square(object):
    """a location on the chess board with potential destinations built in"""

    def __init__(self, file, rank, value, nDest, destinations, destination_order):
        self.file = file
        self.rank = rank
        self.value = value
        self.nDest = nDest
        self.destinations = destinations
        self.destination_order = destination_order
 
    # The informal string definition; contrast __repl__()
    def __str__(self):
        return "file {} rank {}:\nStatus: {}, {} destinations\n".format(self.file, self.rank, self.value, self.nDest)


def Jump(square):
    # This code moves our knight to a new location if possible
    return True

def Dist(a, b):
    distFiles = a[0]-b[0]
    distRanks = a[1]-b[1]
    return abs(distFiles) + abs(distRanks)

print 'oh i see you are here'

jumps = [(-2,-1),(-2, 1),(-1, 2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
nJumps = length(jumps)

nRanks = 8
nFiles = 8
rankList = range(nRanks)
fileList = range(nFiles)
print rankList, fileList

off = square(-1, -1, False, 0, [], [])
board = [off]

for rank in rankList:
    for file in fileList: 
        d = []
        board.append(square(rank, file, False, 1, [off], [0]))
        
print len(board)
for s in board:
    print s



    
 