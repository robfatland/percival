# 
# What this program does
#

import numpy as np
from sys import argv

script, user_name=argv

# this function gives us the denominator of each fraction
def factorial(f):
    if f == 0:
        return 1.0
    else:
        r = 1.0
        for q in range(f):
            r = r * (q + 1)
        return r


# this function gives us the numerator of each fraction
def xtothey(x, y):
    return np.power(x, y)

prompt="Hello, my name is Bozzle mc Dorkins, your host for tonight. Welcome to the random question show! get the questions right, and you win a mamillion dollars!"
print prompt
print "Hi %s, i am the %s script" % (user_name, script)
print "I'd like to ask you a few questions."
print "What is 1 + 1 %s?" % user_name
two = raw_input(">>>")

print "Do you find monsters innterressting %s?" % user_name
innterressting = raw_input()

print "Are we going to Harry Potter World over the summer and are you going to buy me everything i get there just like in Disneyland? %s?" % user_name
computer = raw_input()

print """
Alright. so you said %r about 1 + 1.
You said %r about monsters.
and you %r going to do that. Awsome!!! Have a nice trip!. Annndddd... You win a mamillion dollars! (In your dreams)
""" % (two, innterressting, computer)

# These lines explore the difference between integer and floating point, int() versus float()
# intX = int(x)
# print intX
# y = x / 3
# yy = x / 3.0
# z = intX / 3
# zz = intX / 3.0
# print y, yy, z, zz


# this is which fraction we are on
#y = 0

# etothex = 0.0

# this loops over the fractions. We asked for 'numfrac' of them: 0, 1, 2, ..., numfrac
# while y <= numfrac: 

    #thisnumer = xtothey(x, y)
    #thisdenom = factorial(y)
    #fraction = thisnumer / thisdenom

    # now add the new fraction to the total sum
    #etothex = etothex + fraction

    #print 'y =', y, 'and the fraction is', fraction 
    #y = y + 1



# here at the end we print the sum of the fractions which is e to the x
#   but we are accurate only if we added together enough fractions
#print '\n'
#print 'e to the', x, '=', etothex
#print '\n'
#print 'The official answer is', np.exp(x)
#print '\n'

