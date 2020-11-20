from __future__ import division
#import sys
import os
import matplotlib.pyplot as plt
import scipy
from scipy import special
import numpy as np

mydir = os.path.expanduser("~/")


def root_of_closest_perfect_square(n):
    """ http://stackoverflow.com/questions/15390807/integer-square-root-in-python """

    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x



def iroot(k, n):
    """ http://stackoverflow.com/questions/15978781/how-to-find-integer-nth-roots"""

    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s


def closest_perfect_kth_root(x, k): # x is the number of interest, k is the power
    """ naive method by KJL """

    y = 2
    while y <= x:
        y = y**k
        if y > x:
            return y**(1/k) - 1
        if y == x:
            y**(1/k)

        y = y**(1/k)
        y += 1



def WHL_kth(x, k):
    """ main computing function derived by Kevin Webster, Blane Hollingsworth,
    and Ken Locey """

    n = closest_perfect_kth_root(x, k) # x is the number of interest, k is the power
    i = 1
    a = 0
    while i <= k:
        b = scipy.special.binom(k, 1)
        a += (b*(n**(k-i)))
        i += 1

    a = (x - n**k)/a
    a += n

    return float(a)


def Guess(x, k):
    """ a function to guess the remainder of the root to reveal whether
    decreasing error in the WHL algorithm is meaningful """

    n = closest_perfect_kth_root(x, k) # x is the number of interest, k is the power
    a = np.random.uniform(0,1)
    #a = 0.5
    a += n

    return float(a)
