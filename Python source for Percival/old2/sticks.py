########
#
# Welcome to sticks.py
# 
#   This program draws sticks
#
########

# Keep this line: It gives you the plotting library
import matplotlib.pyplot as plt

# Keep this line: It gives you mathematical functions like sine and cosine
import numpy as np

# Keep this line: It assigns the value of pi (3.1415...) to the variable 'pi'
pi = np.pi




# This gives you a figure and an axis-based plot called 'theAxis'
theFigure, theAxis = plt.subplots(figsize=(14,14))

# This makes your plots be nice and even vertical/horizontal; so a circle looks like a circle, not an egg
theAxis.axis('equal')

# Each of these 'set' commands affects how the plot looks
theAxis.set(xlim=(-3,3), ylim=(-3,3))
theAxis.set(xlabel='x')
theAxis.set(ylabel='y')
theAxis.set(title='coordinate plane')

# This is a single random walk path:
# x = []
# y = []
# for i in range(5):
#     x.append(3*np.random.rand())
#     y.append(3*np.random.rand())
# theAxis.plot(x, y, c='k')

# This is supposed to be five independent line segments
for i in range(5):
    x = [6*np.random.rand()-3]
    x.append(x[0] + 0.1)
    y = [6*np.random.rand()-3]
    y.append(y[0] + 0.1)
    theAxis.plot(x, y, c='k')



# This plots some markers (notice it uses 'scatter()')
# theAxis.scatter(list_of_cosines, list_of_sines, c='orange', s=250, linewidth=1)


# This you should keep: It makes sure we see the plot when all is said and done!
plt.show()

print "yay for sushi!"
