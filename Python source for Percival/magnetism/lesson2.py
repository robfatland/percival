########
#
# Welcome to lesson2.py
# 
#   This program draws some pins on a chart, randomly
#     We use the results of lesson 1 and add in the necessary code to make this chart.
#     To find the lessone: Scroll down to where it says LESSON 2!!!
#
########
#
#########
#
# Setup
#

# The plotting library
import matplotlib.pyplot as plt

# Mathematical functions 
import numpy as np

# This next line gives you a figure and a chart (where your plot goes)
theFigure, theChart = plt.subplots(figsize=(8,8))

# This next line makes the chart even: vertical = horizontal
theChart.axis('equal')

# This 'set' command affects the plot layout:
theChart.set(xlim=(-3.2,3.2), ylim=(-3.2,3.2), xlabel='LION AXIS', ylabel='UNICORN AXIS', title='PIGSTORM!!!')

########
#
# LESSON 2!!!!!
#
########
#
# First read through the entire program to get an idea of what is going on; there
#   are only five lines of actual code up above and 2 lines of code down below for
#   a total of 7. You have to write only about six more lines of code to finish this
#   lesson. Don't be intimidated by this long comment: It is your guide to getting 
#   done quickly.
#
# Next (up above) change the chart x and y axis labels to be something fun... 
#   like 'frogs' and 'pigs' or something. 
#
# The rest of your work goes down below this comment:
# 1. set a variable called nPins equal to 3
# 2. make sure it is really 3 (and then comment out the print statement)
# 3. make a for-loop that runs 'nPins' times (print to be sure, then comment that out)
#     4. inside the loop: set x and y to be random variable on [-3, 3] (print, then comment out)
#     5. set dx and dy to be random variable on [-.2, .2] (print / comment out) 
#     6. convert the above into two lists: xList and yList... (print / comment out)
#          this might look like 'xList = [x, x + dx]'
#
# Now your loop invents a random little pin each time through; but you need to draw the pins.
#   This is the same idea as printing things out but you are printing graphics instead of numbers.
#
#     7. Inside the loop add the pin-print command. It looks like this: 
#
#     theChart.plot(xList, yList, '-', c='r')
#
#     Before you run this guess: 
#       What will the pins look like? 
#       What color will they be?
#
#     You may experiment with the format string '-'. Try 'o-', 'o', '-o'.
#     You may experiment with the color. Try 'g', 'b', 'yellow', 'k'
#     You can make nPins larger if you like, even up to 1000.
#
# Extra: Can the list just be xList = [x]? (and likewise for yList)
#        Can you skip the list like this: theChart.plot(x, y, '-')
#
# Ok below here is where your code goes:
# 
#########

nPins = 3






#
# This last part displays our results
#
plt.show()

#
# This is our hurray!
#
print "yay for sushi!"
