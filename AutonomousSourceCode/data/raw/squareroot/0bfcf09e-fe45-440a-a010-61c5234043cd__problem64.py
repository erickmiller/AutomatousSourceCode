# Odd period square roots
# Problem 64
# All square roots are periodic when written as continued fractions and can be written in the form:


# It can be seen that the sequence is repeating. For conciseness, we use the notation v23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

# The first ten continued fraction representations of (irrational) square roots are:

# v2=[1;(2)], period=1
# v3=[1;(1,2)], period=2
# v5=[2;(4)], period=1
# v6=[2;(2,4)], period=2
# v7=[2;(1,1,1,4)], period=4
# v8=[2;(1,4)], period=2
# v10=[3;(6)], period=1
# v11=[3;(3,6)], period=2
# v12= [3;(2,6)], period=2
# v13=[3;(1,1,1,1,6)], period=5

# Exactly four continued fractions, for N = 13, have an odd period.

# How many continued fractions for N = 10000 have an odd period?

import time
import help
from math import sqrt

def solve(max):
    print(len(list(filter(hasOddRootPeriod, range(1,max+1)))))
    
def hasOddRootPeriod(a):
    return getRootPeriod(a) % 2 == 1

def getRootPeriod(a):
    l = help.conFraction(a)
    return len(l)-1