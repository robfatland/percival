########
#
# Welcome to Math.py
# 
#   This program allows you to experiment with Lists of numbers.
#   In Python a List uses the special symbols [ ] to indicate it is a List.
#   You can say, for example, 
# 
#   a = [1, 2, 3]
#   print a
# 
#     (try it!)
# 
#   The lines of code below each have an explanation. Some lines should stay put.
#   Other lines you can comment out or un-comment to experiment. 
#
########

# Keep this line: It gives you the plotting library
import matplotlib.pyplot as plt

# Keep this line: It gives you mathematical functions like sine and cosine
import numpy as np

# Keep this line: It assigns the value of pi (3.1415...) to the variable 'pi'
pi = np.pi

print pi
mylist=[pi]
print mylist

# Here is our first list. You can change the 3 parameters. Notice that we are 
#   using the numpy library which (up above) we abbreviated 'np'. Here the 
#   method 'arange' has three arguments: start, end and increment. If you said
#   
#   a = np.arange(0.0, 0.8, 0.2) 
# 
#   you would get a list called 'a' that goes 0.0, 0.2, 0.4, 0.6 but not 0.8.
#   The rule is it goes to numbers strictly less than the end. What would you
#   end up with here: 
#
#   a = np.arange(0.0, 0.800000001, 0.2)
#

list_of_thetas = np.arange(0.0, pi/2,.1)

# You can comment/uncomment the print statements to see what is in a list
print list_of_thetas

# Here we assign the cosine of theta to the list of cosines...
list_of_cosines = np.cos(list_of_thetas)

# print list_of_cosines

list_of_sines = np.sin(list_of_thetas)

# print list_of_sines

# check_izzies_idea = list_of_cosines*list_of_cosines + \
#     list_of_sines*list_of_sines
# print check_izzies_idea

# These two lines are very tricky
list_of_furbs = list_of_cosines * list_of_thetas
list_of_gonks = list_of_sines * list_of_thetas

# print list_of_furbs
# print list_of_gonks

# This is a variation on Izzie's idea up above
# list_of_distances = np.sqrt(list_of_furbs*list_of_furbs + list_of_gonks*list_of_gonks)
# print list_of_distances

# This is for reference: It creates 3 plots for the price of one. Leave it be for now
#   (although you can experiment with it if you like) 
# thePlot, theAxes = plt.subplots(3, figsize=(5,5))

# This gives you a figure and an axis-based plot called 'theAxis'
theFigure, theAxis = plt.subplots(figsize=(14,14))

# This makes your plots be nice and even vertical/horizontal; so a circle looks like a circle, not an egg
theAxis.axis('equal')

# Each of these 'set' commands affects how the plot looks
theAxis.set(xlim=(-3,3), ylim=(-3,3))
theAxis.set(xlabel='Daddyland')
theAxis.set(ylabel='Mommyland')
theAxis.set(title='Boomyland"s founders')

# This plots some markers (notice it uses 'scatter()')
theAxis.scatter(list_of_cosines, list_of_sines, c='orange', s=250, linewidth=1)

# This plots some lines (notice it uses 'plot()')
theAxis.plot(list_of_cosines, list_of_sines, c='k')
theAxis.scatter(list_of_cosines, list_of_sines, c='brown', s=100, linewidth=1)

# Here are the furbs and gonks
# plt.plot(list_of_furbs, list_of_gonks)

bbx= [.1,.3,.2,0,.1]
bby= [.1,.8,1.5,.9,.1]
theAxis.plot(bbx,bby)

# This you should keep: It makes sure we see the plot when all is said and done!
plt.show()

print "blah"
