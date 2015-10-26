# Knight Tour
# 
# An 8 x 8 chess board is empty save for a lone knight on one corner. Can the knight make
#   63 moves and visit each remaining square of the board once?
#
# The answer is yes and writing code to solve the problem is an interesting two-stage 
#   exercise (the way I approach it). I have solved this problem at least three times 
#   using the C programming language; but Python is remarkably adapted to it and the
#   solution given here is comparatively simpler than my old C solutions.
# 
# Wikipedia has a nice article that includes generalizations to other rectangular boards:
# 
# "Schwenk proved that for any m × n board with m ? n, a closed knight's tour is always possible unless 
#   one or more of these three conditions are met:
#     1. m and n are both odd
#     2. m = 1, 2, or 4
#     3. m = 3 and n = 4, 6, or 8"
# 
# This program does not look for closed tours (that loop back on themselves); and with a few extra 
#   minutes I explored some square boards and found that of course 2 x 2 and 3 x 3 boards are not
#   solvable, nor is a 4 x 4. A 9 x 9 board runs for several minutes without solving as do 13 x 13
#   and 14 x 14 boards. In contrast all other n x n boards up to 20 x 20 solve in a few seconds at most.
#
# The first stage of the solution is to create a means of exploring possible solutions.
# 
# The second stage of the solution is to apply a heuristic to the move orders. Allow me
#   to explain: From each square there are between 2 and 8 possible knight moves; more 
#   when one is in the center of the board. Exploring them by trial and error requires
#   bookkeeping to determine if a possible destination square has already been visited 
#   in the tour. In real life the visited squares are marked for example using pennies. 
# 
#   Using the same ordering for each square creates a bias in the search pattern that 
#   proves un-productive: The knight winds up exploring many many avenues which do not
#   come remotely close to a solution; and hence the problem is not solved by the program.
#
#   What I found interesting is that the possible destination squares can be prioritized
#   by a simple heuristic that leads almost immediately to a correct solution by the program.
#   This heuristic is: Always move as far from the center of the board as possible. 
# 
#   In the code below there is a call to the SortOrder() method that formalizes this 
#   heuristic. Moves from a given square will be tried in an order giving preference to 
#   heading to the perimeter of the board. After the order has been sorted a single
#   recursive method called Move() is called which is only seven lines of code in its
#   minimized ('MoveMinimalist()') form. Seven lines! 
# 
# Python Programming
# The idea here is to work with classes, tuples and lists.
#   Starting point: A location on the chess board is a (file, rank) tuple
#   A knight move (jump) is a relative tuple. This is analogous to date times and time intervals.
#     Note: '+' is treated as 'concatenate' so tuples can not be added out of the box.
#

import sys          # used to halt the program
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



# Define the chess board (as a square; but this is easily modified to rectangular boards)
edge = 8
nRanks = edge
nFiles = edge
rankList = range(nRanks)
fileList = range(nFiles)

# An arbitrarily ordered List of possible knight moves as relative (d-file, d-rank)
jumps = [(-2,-1),(-2, 1),(-1, 2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]

# The board will be a list of squares, each of whom knows where a knight can go from there
board = []

# The tour will be a list of board square indices, as in: index = file*nRanks + rank
tour = []

# off is a location that is not on the chessboard, for convenience
off = (-1, -1)





# The square class describes a given square on the chess board
class square(object):
    """a location on the chess board with potential destinations built in"""

    def __init__(self, loc, value, destinations, order, metric):
        self.loc = loc                       # tuple (file, rank)
        self.value = value                   # occupied / visited
        self.destinations = destinations     # where a knight could go from here
        self.order = order                   # destinations are prioritized here
        self.metric = metric                 # city block distance from center of board
 
    # The informal string definition; contrast __repl__()
    def __str__(self):
        return "file {} rank {}:\nStatus: {}, {}, {} destinations\n".format(self.loc[0], self.loc[1], self.value, self.metric, len(self.destinations))

# These are not used but could be used to modify how destination sorting is done by SortOrder()
square.__eq__ = lambda self, other: self.metric == other.metric
square.__ne__ = lambda self, other: self.metric != other.metric
square.__lt__ = lambda self, other: self.metric < other.metric
square.__le__ = lambda self, other: self.metric <= other.metric
square.__gt__ = lambda self, other: self.metric > other.metric
square.__ge__ = lambda self, other: self.metric >= other.metric

# To use city-block distance we need a center square. I make this a little bit 
#   unnecessarily complicated by using 'the closest of any of the four center squares'.
#   It would probably work fine to just use (3, 3). 
# Also this is jury-rigged for odd-size boards!
def GetClosestCenter(s):
    if edge%2 == 1: return (edge/2, edge/2)
    if s[0] < edge/2:
        if s[1] < edge/2:
            return (edge/2 - 1, edge/2 - 1)
        else:
            return (edge/2 - 1, edge/2)
    else:
        if s[1] < edge/2:
            return (edge/2, edge/2 - 1)
        else:
            return (edge/2, edge/2)

# City block distance to the center of the board
def Metric(a):
    b = GetClosestCenter(a)
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


# onboard returns a hypothetical jump location if it is on the board or 'off' (-1, -1) if not
def OnBoard(s, j):
    hypo = (s.loc[0] + j[0], s.loc[1] + j[1])
    if hypo[0] >= 0 and hypo[0] < nFiles and hypo[1] >= 0 and hypo[1] < nRanks:
        return hypo
    else:
        return off

# Create 64 squares in board[]
# To accomplish consistent index-to-coordinates mapping: files *must* be in the outer loop
def CreateBoard():
    for file in fileList:
        for rank in rankList: 
            s = square((file, rank), False, [], [], 0)
            for j in jumps:
                next = OnBoard(s, j)
                if next != off:
                    s.destinations.append(next)
                    s.order.append(len(s.destinations) - 1)
            s.metric = Metric(s.loc)
            board.append(s)

def PrintTour():
    print "\n\n\nHi there! I print the tour and then halt!\n\n\n\n"
    for sq in range(len(tour)):
        index = tour[sq]
        print 'move ', sq + 1, ' --> file ', board[index].loc[0], ', rank ', board[index].loc[1]
    print "\n\n\n"

    # Some fragmentary code to draw the chess board as a grid and so on
    #display = np.ones((nFiles, nRanks)) * 0
    #display[3, 7] = 2
    #fig, ax = plt.subplots(1, 1, tight_layout=True)
    #for x in range(nRanks + 1):
    ##   ax.axhline(x, lw=2, color='black', zorder=5)
    #for y in range(nFiles + 1):
    #    ax.axvline(y, lw=2, color='black', zorder=5)
    #my_cmap = matplotlib.colors.ListedColormap(['white', 'g', 'b'])
    #ax.imshow(display, interpolation='none', cmap = my_cmap, extent=[0, nFiles, 0, nRanks], zorder=0)
    #ax.axis('off')
    #plt.show()

    wait = raw_input("enter to see tour")
    plt.axes([0,0,1,1])
    size = 16
    scaleX = 0.9 / (nFiles - 1.0)
    scaleY = 0.9 / (nRanks - 1.0)
    for sq in range(len(tour)):
        index = tour[sq]
        # print 'move ', sq + 1, ' --> file ', board[index].loc[0], ', rank ', board[index].loc[1]
        text = str(sq + 1)
        x = 0.05 + scaleX * board[index].loc[0]
        y = 0.05 + scaleY * board[index].loc[1]
        plt.text(x, y, text, ha='center', va='center', color="#000000", alpha=1.0, transform=plt.gca().transAxes, fontsize=size, clip_on=True)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    wait = raw_input("enter to halt")
    sys.exit(0)

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
    if tourLen == nRanks * nFiles:
        print "\n\nTime to celebrate!\n\n\n\n\n"
        PrintTour()
        sys.exit(0)
    # else:
    #     if tourLen == 20 or tourLen == 30 or tourLen == 40 or tourLen == 50:
    #         PrintTour()

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

# This is the same code as Move() reduced to a minimal number of lines
def MoveMinimalist(s):
    tour.append(LocToIdx(s.loc))    # tour[] is a growing list of board square indices (integers)
    s.value = True                  # now that we're here let's mark this square 'visited'
    if len(tour) == nRanks * nFiles: PrintTour()
    for ordinal in s.order: 
        if board[LocToIdx(s.destinations[ordinal])].value == False: MoveMinimalist(board[LocToIdx(s.destinations[ordinal])])
    tour.pop()
    s.value = False

# SortOrder implements a heuristic: Prioritize moves towards the perimeter of the board
# An elegant thing would be to sort .order based on .metric
# This doesn't work: s.order.sort(key=board[LocToIdx(s.destinations[s.order[]])].metric)
# Another thing would be to use the built-in comparatives for squares (see top of this file)
# My current solution is rather pedestrian!
def SortOrder():
    for s in board:
        found = [0] * len(s.destinations)
        for i in range(len(s.destinations)):
            best = -1000    # A terrible score indeed
            bestIdx = -1    # A non-existent index; note the code presupposes a best proper index will be found
            for j in range(len(s.destinations)):
                if found[j] == 0:
                    thisMetric = board[LocToIdx(s.destinations[j])].metric
                    if best < thisMetric:
                        best = thisMetric
                        bestIdx = j
            s.order[i] = bestIdx
            found[bestIdx] = 1


# This, believe it or not, is the actual program as such
CreateBoard()
SortOrder()
MoveMinimalist(board[0])
print '\n\nI guess this ', nRanks, ' x ', nFiles, 'board is unsolvable!\n\n\n'
sys.exit(0)

