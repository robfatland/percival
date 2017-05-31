########
#
# Welcome to field.py
# 
#   This program draws iron filings in response to a magnetic field
#
########

#########
#
# Setup
#
#

# The plotting library
import matplotlib.pyplot as ...

# Mathematical functions like sine and cosine
import numpy as ..

# Keep this line: It assigns the value of pi (3.1415...) to the variable 'pi'
pi = np...

#
# 
#########
#
# Two useful functions for vectors
#
#

# This takes a vector and returns its length
def Length(a, b):
    return np.sqrt(........

# This takes a vector and changes its length to 1 without changing its direction
def Norm(a, b):
    if a == 0 and b == 0: return 0, 0
    len = ............
    return ......, ......

#
#
#########
#
# Setting up the figure
#
#

# This gives you a figure and an axis-based plot called 'theAxis'
theFigure, theAxis = plt.subplots(figsize=(14,14))

# This makes your plots be nice and even vertical/horizontal; so a circle looks like a circle, not an egg
theAxis.axis('equal')

# Each of these 'set' commands affects how the plot looks
theAxis.set(xlim=(-3.2,3.2), ylim=(-3.2,3.2))
theAxis.set(xlabel='x')
theAxis.set(ylabel='y')
theAxis.set(title='magnetic field')

#
#
#########
#
# Drawing the field by dropping filings
#
#

# How many iron filings do we want to drop on the sheet of paper?
nFilings = 7

# scale makes our filings have a length of 0.15... or whatever we like
scale = 0.15

for i in range(nFilings):

    # we choose a random location for two coordinates x and y
    # uses np.random.rand()... 
    x = ............................
    y = ............................

    # now we calculate the field vector (dx, dy)
    r = ...........
    rCubed = np.power(.......)
    rFifth = np.power(.......)
    dx = ..............
    dy = .................................

    # now we shorten the field vector to the length of a filing in two steps
    #   1. Make it have length 1
    #   2. Scale it down using our 'scale' factor
    dxN, dyN = .................
    dxN *= .....
    dyN *= .....

    # Plot this filing
    theAxis.plot([x, x + dxN], [y, y + dyN], c='k' )

#
#
###########
#
# Finishing up
#
#

# This makes sure we see the plot when all is said and done!
plt.show()

print "yay for sushi!"
