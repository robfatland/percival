########
#
# Welcome to lesson1.py
# 
#   This program generates some random numbers!
#   It was completed by The Boom on March 27 2016.
#
########

#########
#
# Setup
#
#

# The plotting library
import matplotlib.pyplot as plt

# Mathematical functions like sine and cosine
import numpy as np

# ok let's count to some number... 
#   np.random.uniform() is on 0 to 1
# as we count let's generate a random number for x and another for y
# let's make them go from 0 to 7
# let's make them go from -6 to 6 


nBooms = 10
for Boomy in range(nBooms):
    print "Da frog!", Boomy
    x=np.random.uniform()*12 - 6
    print "x=", x
    y=np.random.uniform()*12 - 6
    print "y=", y
