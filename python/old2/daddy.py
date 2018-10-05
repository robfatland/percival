import matplotlib.pyplot as plt
import numpy as np

############
#
# Some legacy code on simple string interactivity
#
############
#
# from sys import argv
#
# This is a tuple that will crash the program without a second cla!
# script, user_name = argv
# prompt = '> '
# print "Hi %s, i am the %s script" % (user_name, script)
#
# This is a prompt to string input
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)
#
# This is a multi-line print:
# print """
# Alright. so you said %r about liking me.
# You live in %r. not sure where that is.
# and you have a %r computer. nice.
# """ % (likes, lives, computer)
#
###########

pi = np.pi
theta=np.arange(0.0, 4.0*pi, 0.1)
r = theta
x = r*np.cos(theta)
y = r*np.sin(theta)

# t = np.arange(0.0, 2.0, 0.01)
# s = np.sin(2*np.pi*t)

plt.subplot(2,1,1)
plt.plot(x, y)

plt.subplot(2,1,2)
plt.plot(theta, x)
plt.show()

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
