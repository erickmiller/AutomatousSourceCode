#!/usr/bin/env python
#coding:utf-8

"""
Square root digital expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

"""
from decimal import *

def digitalSumOfSquareNum(n,k):
    getcontext().prec=k
    digits=list(str(Decimal(n).sqrt()).replace('.','')[:-2])
    digits=[int(i) for i in digits]
    return sum(digits)

def answer():
    total=0
    for n in set(range(2,100))-set([i**2 for i in xrange(10)]):
        total+=digitalSumOfSquareNum(n,102)
    print total

import time
tStart=time.time()
answer()
print 'run time=',time.time()-tStart
# 40886
# run time= 0.0131640434265
