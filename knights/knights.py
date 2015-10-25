nRanks = 8
nFiles = 8
rankList = range(nRanks)
fileList = range(nFiles)
print rankList, fileList

jumps = [(-2,-1),(-2, 1),(-1, 2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
nJumps = len(jumps)
board = []
tour = []

off = (-1, -1)

# The idea here is to work with classes, tuples and lists in a fairly useful way
# Starting point is that a location is a (file, rank) tuple
# A jump is a relative tuple, same order of course. Unfortunately '+' is treated as 'concatenate'.

class square(object):
    """a location on the chess board with potential destinations built in"""

    def __init__(self, loc, value, destinations, order, flipdist):
        self.loc = loc                       # tuple (file, rank)
        self.value = value                   # occupied / visited
        self.destinations = destinations     # where a knight could go from here
        self.order = order                   # destinations are prioritized here
        self.flipdist = flipdist             # city block distance from center of board
 
    # The informal string definition; contrast __repl__()
    def __str__(self):
        return "file {} rank {}:\nStatus: {}, {} destinations\n".format(self.loc[0], self.loc[1], self.value, len(self.destinations))

def GetClosestCenter(s):
    if s[0] < 4:
        if s[1] < 4:
            return (3, 3)
        else:
            return (3, 4)
    else:
        if s[1] < 4:
            return (4, 3)
        else:
            return (4, 4)

def Distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def FlippedDistance(distance):
    return -distance

# onboard returns a new jump location if it is on the board or (-1, -1) if not
def OnBoard(s, j):
    hypo = (s.loc[0] + j[0], s.loc[1] + j[1])
    if hypo[0] >= 0 and hypo[0] < nFiles and hypo[1] >= 0 and hypo[1] < nRanks:
        return hypo
    else:
        return off

print 'oh i see you are here'

# Create 64 squares in board[]
# To accomplish consistent index-to-coordinates mapping: files *must* be in the outer loop
for file in fileList:
    for rank in rankList: 
        s = square((file, rank), False, [], [], 0)
        for j in jumps:
            next = OnBoard(s, j)
            if next != off:
                s.destinations.append(next)
                s.order.append(len(s.destinations) - 1)
        s.flipdist = FlippedDistance(Distance(s.loc, GetClosestCenter(s.loc)))
        board.append(s)
        
# print len(board)
# for s in board: print s

def PrintTour():
    print "\n\n\n"
    for sq in range(len(tour)):
        index = tour[sq]
        print 'move ', sq + 1, ' --> file ', board[index].loc[0], ', rank ', board[index].loc[1]
    print "\n\n\n"
    return  

def LocToIdx(s): return s[0]*nRanks + s[1]

def Move(s):
    # We are passed a square s
    # The value here better already by True
    # Starting at the top (Kilroy: Need order here) of s's destination List we try 
    #   to find one that is open. 
    #     If so we go there by calling Move() recursively.
    #     If not we are stuck and must back up.
    # The state variables we care about are tour (a List that grows and shrinks as we make progress)
    #   and the Bool values of a potential destination squares. And of course the squares themselves.
    # I still do not have a good way around converting file and rank to square index...
    #

    tour.append(LocToIdx(s.loc))    # tour[] is a growing list of board square indices (integers)
    s.value = True                  # now that we're here let's mark this square 'visited'

    # Let's check first whether we are done solving the knight's tour puzzle
    tourLen = len(tour)
    if tourLen == 64:
        print "\n\nTime to celebrate!\n\n\n\n\n"
        PrintTour()
        sys.exit(0)
    else:
        if tourLen == 20 or tourLen == 30 or tourLen == 40 or tourLen == 50:
            PrintTour()

    for ordinal in s.order:                   # So ordinal is an index into the destinations list
        d = s.destinations[ordinal]           # So d is the next recommended destination to try
        destIdx = LocToIdx(d)                 # So destIdx is the index of that square
        if board[destIdx].value == False:
            Move(board[destIdx])

        # At this point we've either gone off deeper into the board or we haven't.
        #   If we did go off deeper into the board...
        #       If we never return back to here then the puzzle was solved
        #       If we did wind up back here it is time to press on with the ordinal loop
        #   If we did not go deeper into the board...
        #       Then it is time to press on with the ordinal loop

    # Now at this point we have fallen out of the ordinal loop so we had better back up
    tour.pop()
    s.value = False
    return

def MoveMinimalist(s):
    tour.append(LocToIdx(s.loc))    # tour[] is a growing list of board square indices (integers)
    s.value = True                  # now that we're here let's mark this square 'visited'
    tourLen = len(tour)
    if tourLen == 64:
        PrintTour()
        sys.exit(0)
    for ordinal in s.order:                                   # So ordinal is an index into the destinations list
        destIdx = LocToIdx(s.destinations[ordinal])           # So destIdx is the index of the next square to try
        if board[destIdx].value == False:
            Move(board[destIdx])
    tour.pop()
    s.value = False
    return

import numpy as np

def SortOrder():
    for s in board:
        nd = len(s.destinations)
        found = [0] * nd
        for i in range(nd):
            best = -1000
            bestIdx = -1
            for j in range(nd):
                if found[j] == 0:
                    thisFlipDist = board[LocToIdx(s.destinations[j])].flipdist
                    if best < thisFlipDist:
                        best = thisFlipDist
                        bestIdx = j
            s.order[i] = bestIdx
            found[bestIdx] = 1


        # An elegant thing would be to sort .order based on .flipdist
        # This doesn't work: s.order.sort(key=board[LocToIdx(s.destinations[s.order[]])].flipdist)
        # for d in range(len(s.destinations)):
            # oh bugger
    return

# This, believe it or not, is the actual program as such
SortOrder()
Move(board[0])

