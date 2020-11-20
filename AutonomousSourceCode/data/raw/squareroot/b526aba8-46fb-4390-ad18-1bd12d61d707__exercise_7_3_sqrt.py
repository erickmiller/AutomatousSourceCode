#! /usr/bin/python
#
# From http://greenteapress.com/thinkpython/html/thinkpython008.html
# Chapter 7 exercise 3
# Implement Newton's method to find square roots
#
import math

epsilon = 1.0E-12

def sqrt ( x ) :
    while True:
#        print x
        y = (x + a/x) / 2
        if abs(y-x) < epsilon :
            break
        x = y
    return y


def test_square_root( a ) :
    xt = sqrt(a)
    xc = math.sqrt(a)
    print "%10f %14f %14f %10.4e" % ( a, xt, xc, abs( xc-xt) ) 

for a in range(1,10) :
    test_square_root( float(a) )


