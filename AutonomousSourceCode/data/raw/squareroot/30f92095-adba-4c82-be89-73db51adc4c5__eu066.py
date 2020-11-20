#!/usr/bin/python
# encoding: utf-8
"""
project euler (projecteuler.net) problem 66
solution by Kevin Retzke, May 2012
"""
import math

#squares = set()

def isSquare(n):
    #if n in squares:
    #    return True
    root = math.sqrt(n)
    if int(root + 0.5)**2 == n:
        #squares.add(n)
        return True
    return False

def diophantine(d):
    """Determines the minimum solution of x for the equation
    x**2 - Dy**2 = 1"""
    x = 2
    while True:
        num = x*x-1
        if num%d == 0 and isSquare(num/d):
            return x
        x += 1

if __name__ == '__main__':
    assert map(diophantine, [2,3,5,6,7]) == [3,2,9,5,8]
    maxx = 0
    maxd = 0
    for d in xrange(2,62):
        if isSquare(d):
            continue
        x = diophantine(d)
        print d, x
        if x > maxx:
            maxx = x
            maxd = d
            #print maxd, maxx
    print maxd
            
