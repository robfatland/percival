# 
# What this program does
#

import numpy as np
from sys import argv

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




script, stringX, stringNumfrac = argv

x = float(stringX)
numfrac = int(stringNumfrac)

print 'you entered a value of x =', x

# These lines explore the difference between integer and floating point, int() versus float()
# intX = int(x)
# print intX
# y = x / 3
# yy = x / 3.0
# z = intX / 3
# zz = intX / 3.0
# print y, yy, z, zz


# this is which fraction we are on
y = 0

etothex = 0.0

# this loops over the fractions. We asked for 'numfrac' of them: 0, 1, 2, ..., numfrac
while y <= numfrac: 

    thisnumer = xtothey(x, y)
    thisdenom = factorial(y)
    fraction = thisnumer / thisdenom

    # now add the new fraction to the total sum
    etothex = etothex + fraction

    print 'y =', y, 'and the fraction is', fraction 
    y = y + 1



# here at the end we print the sum of the fractions which is e to the x
#   but we are accurate only if we added together enough fractions
print '\n'
print 'e to the', x, '=', etothex
print '\n'
print 'The official answer is', np.exp(x)
print '\n'

