##################
#
# Welcome to torus dot py
#
# This program is shows a grid of cells and uses a method to populate them
#   with symbols; and then they change over time. It is based on timestep.py.
# Here are some sub-objectives chosen on the command line...
#   - with no command line arg: Display options and halt
#   - with 1 [N = 200]: have a dot move on a diagonal trajectory for N timesteps
#   - with 2: Knight's tour
#   - with 3 [density]: do Life
#   - with 4 [ratio]: WaTor
#
###################
#
# The assignment line, = theAxis.plot([], [], lw=2) is shorthand for 'assign line to the first element of the returned 
#   list or array (JVDP personal communication). This could be expanded to a list by removing the comma. Furthermore
#   the arguments to plot can be expanded out so that each element of that list is unique; they are not necessarily 
#   all carbon copies of one another.
# In the plot() call notice that 'lw' and 'linewidth' both mean linewidth, and have idiosyncratic meanings... 
# Incidentally: 'line' is officially an 'artist' sub-class. 
#   It would be worthwhile documenting the best way to bootstrap all of this information (kilroy) in case one 
#   does not have Jake nearby. 
# Cursor click location methods can be found by searching 'python cursor click callback'. (kilroy doc this also!)
#   One approach seems to be through OpenCV starting with import cv.
# The scatter (rather than 'plot()' approach will also work but care is necessary in the accompanying 'matlab-like' 
#   arguments. Notice I originally commented it out because it did not seem to work; but actually it can be 
#   coerced into working with some more scrutiny.
# 
####################

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

# for command line and halting properly
import sys
from sys import argv

global_grid = 100
global_gridmod = global_grid + 1
global_x = [0]
global_y = [0]
global_x_start = 40
global_y_start =  3

life_cells = 100
life_density = 0.25

life = np.zeros((life_cells, life_cells), np.int32)
newlife = np.zeros((life_cells, life_cells), np.int32)

global_wator_cells = 120
global_wator = np.zeros((global_wator_cells, global_wator_cells), np.int32)
global_wator_next = np.zeros((global_wator_cells, global_wator_cells), np.int32)

################
#
# utility methods for animation
#
################

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def diagonal_animate(i):
    global_x[0] = (i+global_x_start)%global_gridmod
    global_y[0] = (i+global_y_start)%global_gridmod
    line.set_data(global_x, global_y)
    return line,

# initialize life
def life_init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
# def life_animate(frameNumber, life, newlife):
def life_animate(frameNumber):

    if frameNumber > 0:
      for i in range(life_cells-2):
        ii = i + 1
        for j in range(life_cells-2):
          jj = j + 1

          # nmo = (i - 1)%life_cells
          # n   = i
          # npo = (i + 1)%life_cells
          # mmo = (j - 1)%life_cells
          # m   = j
          # mpo = (j + 1)%life_cells

          # m is the row index aka j coordinate; n is the col index aka i coordinate
          nmo = i - 1
          n   = i
          npo = i + 1
          mmo = j - 1
          m   = j
          mpo = j + 1

          if nmo == -1: nmo = life_cells - 1
          if npo == life_cells: npo = 0
          if mmo == -1: mmo = life_cells - 1
          if mpo == life_cells: mpo = 0

	  sum = life[nmo][mmo]
	  sum += life[nmo][m]
	  sum += life[nmo][mpo]
	  sum += life[n][mmo]
	  sum += life[n][mpo]
	  sum += life[npo][mmo]
	  sum += life[npo][m]
	  sum += life[npo][mpo]

	  if life[i][j] == 0:
            if sum == 3: newlife[i][j] = 1
	    else: newlife[i][j] = 0
	  else:
            if sum == 2 or sum == 3: newlife[i][j] = 1
	    else: newlife[i][j] = 0
          
      # Can not assign 'life = newlife' as this makes a new instance of 'life[][]' that overrides
      #   the global variable; so you just get an 'unassigned' error up above
      life[:] = newlife

      # test: this works
      # for i in range(life_cells):
        # for j in range(life_cells):
          # if np.random.rand() < life_density:
            # life[i][j] = 1
          # else:
            # life[i][j] = 0

    x = []
    y = []
    nAlive = 0
    for i in range(life_cells):
      for j in range(life_cells):
        if life[i][j] == 1:
          x.append(i)
          y.append(j)
          nAlive += 1
    print 'nAlive sez life_animate() = ', nAlive, 'and frameNumber = ', frameNumber
    line.set_data(x, y)
    return line,

# grid initialize
def init_grid(nCells, lw_value):
  global_grid = nCells
  global_gridmod = global_grid + 1
  theFigure, theAxis = plt.subplots(figsize=(14,14))
  for fid in np.arange(-.5, nCells - 1.0 + 0.5 + 0.001, 1.0):
    theAxis.plot([-.5, nCells - 1.0 + 0.5], [fid, fid], c='k')
    theAxis.plot([fid, fid], [-.5, nCells - 1.0 + 0.5], c='k')
  theAxis.axis('equal')
  line, = theAxis.plot([], [], 'o', lw=lw_value)
  return line, theFigure
  
############
#
# Some simple command line processing
#
############

if len(argv) == 1:
  print '\n\nI will tell you what you can do here...'
  print 'torus 1 [N (100)] will draw a grid and a moving dot, N timesteps, 100 by default'
  # sys.exit('\nhalting with no args :)\n\n')
  print 'choosing 3 (Life) by default!\n\n'
  choice = '3'
else:   
  # start parsing
  script = argv[0]
  choice = argv[1]

if choice == '1':
  ###############
  #
  # Diagonally moving dot
  #
  ###############
  print "\nchose simple diagonal animation on torus.\n\n"
  N_timesteps = 200
  if len(argv) > 2:
    test = int(argv[2])
    if test > 0 and test < 10000:
      N_timesteps = test
      print 'cla overrides 100 to set timesteps = ', N_timesteps

  line, fig = init_grid(global_grid, 2)
  anim = animation.FuncAnimation(fig, diagonal_animate, init_func=init, frames=N_timesteps, interval=0, blit=True)
  plt.show()


elif choice == '2':
  ###############
  #
  # Knight's Tour
  #
  ###############
  print "\nchose Knight's Tour\n\n"

elif choice == '3':
  ###############
  #
  # Conway's Life
  #
  ###############
  print "\nchose Conway's Life\n\n"
  N_timesteps = 40
  if len(argv) > 2:
    test = float(argv[2])
    if test > 0.0 and test < 1.0:
      life_density = test
      print 'cla overrides 0.3 to set density = ', life_density
    else:
      print 'default life density = ', life_density

  # life = np.zeros((life_cells, life_cells), np.int32)
  # newlife = np.zeros((life_cells, life_cells), np.int32)
  nAlive = 0
  for i in range(life_cells):
    for j in range(life_cells):
      if np.random.rand() < life_density:
        life[i][j] = 1
        nAlive += 1
      else:
        life[i][j] = 0
  print 'there are these many live cells: ', nAlive

  line, fig = init_grid(life_cells, 1)
  # anim = animation.FuncAnimation(fig, life_animate, fargs = (life, newlife), \
    # init_func=life_init, frames=N_timesteps, interval=0, blit=True)
  anim = animation.FuncAnimation(fig, life_animate, init_func=life_init, \
    frames=N_timesteps, interval=0, blit=True)
  plt.show()


else:
  ###############
  #
  # ????????????
  #
  ###############
  print '\nchose unrecognized choice\n\n'

sys.exit('\n\nyo\n')


