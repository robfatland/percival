###################
#
# Welcome to timesteps dot py
#
# This program is supposed to show a grid of cells and use a method to populate them
#   with symbols; and then they change over time.
#
###################
#
# kilroy hanging problems
# For CA is 'animate' the best option?
# Suppose we want to do knight's tour: here each time step adds or removes a marker...
#   How does this play with the blit logic?
# in Rpi-land halting the plot produces some sort of error verbiage ending with 'tk'...
#   How do I halt this gracefully after 1 time through? n times through? External halt?
# I can't seem to really speed things up by making the animation very lightweight...
# The assignment line, = theAxis.plot([], [], lw=2) seems to use tuple notation; true? why?
#   Could this be augmented to lineA, lineB, lineC, lineD = theAxis.plot([], [], lw=2) thereby... all the same?
#     Could this be done as a list of indexable lines?
#   why 'lw' and not 'linewidth' in the initialization of line?
#   what kind of animal is 'line' here? It seems to be a plot subservient to the axis subservient to the figure. 
#   how can I bootstrap this information rather than asking JVDP?
#   why do init() and animate() return line, ?
# How do I register cursor click locations? The idea is an initialization that populates an array...
#   Is the 'o' construction the only way to register a set of dots (per line, and .plot)?
# 

"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation 

############
#
# Some simple command line processing
#
############

from sys import argv
 
# Don't crash the damn program; deal with no-args
if len(argv) == 1:
  print '\n\nI will proceed with 100 time steps...\n\n'
  # sys.exit('\nhalting with no args :)\n\n')
  numsteps = 100
else:
  script, str_numsteps = argv
  numsteps = int(str_numsteps)

print 'You will have ', numsteps, 'time steps.'

# This gives you a figure and an axis-based plot called 'theAxis'
theFigure, theAxis = plt.subplots(figsize=(8,8))

line, = theAxis.plot([], [], 'o', lw=2)

# Kilroy the following is 'not iterable'...
# dots, = theAxis.scatter([], [], lw=4)

# This makes your plots be nice and even vertical/horizontal; so a circle looks like a circle, not an egg
theAxis.axis('equal')

# alternative to a manual grid (done below but may or may not be commented out)
#   This gives dashed grid lines at a pleasant spacing (but not good CA cells without some further finesse)
# theAxis.grid()

# Each of these 'set' commands affects how the plot looks
# theAxis.set(xlim=(loBound,hiBound), ylim=(loBound-ySlack,hiBound+ySlack))
# theAxis.set(xlabel='x')
# theAxis.set(ylabel='y')
# theAxis.set(title='coordinate plane')

# x = []
# y = []

# Commenting out scribble
# for i in range(20):
#     x.append(loBound + hiBound*np.random.rand())
#     y.append(loBound + hiBound*np.random.rand())
# theAxis.plot(x, y, c='k')

# Grid
loBound = 0.0
hiBound = 100.0
inc = 4.0
ySlack = 10.0
xStretch = 1.0/24.0
for fid in np.arange(loBound, hiBound + inc/2, inc):
    theAxis.plot([loBound, hiBound], [fid, fid], c='k')
    theAxis.plot([fid, fid], [loBound, hiBound], c='k')


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(loBound, hiBound, 7)
    y = (hiBound/2) + (hiBound/2)*np.sin(2 * np.pi * (x * xStretch - 0.01 * i))
    line.set_data(x, y)
    return line,


# call the animator.  blit=True means only re-draw the parts that have changed.
#   anim is a variable, assigned, which causes the animation to persist
#   theFigure is of course the figure we got above
#   animate is the animation of the data structure in terms of the next static frame.
#     It is called once per frame; 
#     It is passed an integer frame index (that it refers to as 'i')
#     It returns the populated 'line' which is initialized above using theAxis.
#   init_func is called once to set things up, specifically to establish line's data as nothing
#     Notice there is some tuple voodoo with line, both returned from init() and from animate()
#   frames is the number of frames to run (and then the animation starts over again)
#   interval is a between-frame pause in milliseconds... i think
#   blit is a boolean that means 'redraw only the parts of the plot that have changed' 
#     making it true speeds up the animation a great deal
anim = animation.FuncAnimation(theFigure, animate, init_func=init, frames=numsteps, interval=100, blit=True)

plt.show()

# legacy code from here down .............................

# This plots some markers (notice it uses 'scatter()')
# theAxis.scatter(list_of_cosines, list_of_sines, c='orange', s=250, linewidth=1)

# theta=np.arange(0.0, 4.0*pi, 0.1)
# r = theta
# x = r*np.cos(theta)
# y = r*np.sin(theta)

# t = np.arange(0.0, 2.0, 0.01)
# s = np.sin(2*np.pi*t)

# plt.subplot(2,1,1)
# plt.plot(x, y)

# plt.subplot(2,1,2)
# plt.plot(theta, x)
# plt.show()

# 
# This next part (when complete) shows axis labels
#   I think the subplot() calls above need to be re-done...
# axis.xlabel('x')
# axis.ylabel('y')
# axis.title('ta da')
# axis.grid(True)
# plt.show()
#
# Alternate reality: Straight up plt.plot(x, y):
#
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('ta da')
# plt.grid(True)
# plt.savefig("test.png")
# plt.show()
#
