########
#
# Welcome to runaround.py
# 
#   This program draws dots connected by sticks that move around
#   It relies on the very famous computer programmer Jake VanDerPlas.
#   Say 'Yay Jake!!!!'
#
########
"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

# This line gives you the plotting library
import matplotlib.pyplot as plt

# This line gives you mathematical functions like sine and cosine
import numpy as np

# This line gets us the ability to animate things
from matplotlib import animation 

# Keep this line: It assigns the value of pi (3.1415...) to the variable 'pi'
pi = np.pi


############
#
# Some simple command line processing
#
############

from sys import argv
 
# This is a tuple that will crash the program without a second cla!
script, str_numdots = argv
numdots = int(str_numdots)
print 'You entered ', numdots, 'dots.'

# This gives you a figure and an axis-based plot called 'theAxis'
theFigure, theAxis = plt.subplots(figsize=(14,14))

line, = theAxis.plot([], [], 'o-', lw=2)

# This makes your plots be nice and even vertical/horizontal; so a circle looks like a circle, not an egg
theAxis.axis('equal')
theAxis.set(xlim=(-1.0,7.0), ylim=(-4,4))

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0.0, 2.0*pi, numdots)
    y = np.sin(x  - 0.05 * i)
    line.set_data(x, y)
    return line,

# def animate2(i):
    # for n in range(numdots):
    # x = np.random.rand() - 0.5

anim = animation.FuncAnimation(theFigure, animate, init_func=init, frames=100, interval=0, blit=True)

plt.show()

