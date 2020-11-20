#! /usr/bin/python
#
# From http://greenteapress.com/thinkpython/html/thinkpython008.html
# Chapter 7 exercise 2
# Implement Newton's method to find square roots
#

epsilon = 1.0E-12

def sqrt ( x ) :
    while True:
        print x
        y = (x + a/x) / 2
        if abs(y-x) < epsilon :
            break
        x = y
    return y

while True :
    a = float( raw_input ( "Enter a value to the take the square root of " ) )
    x = sqrt(a)
    e = a - x*x
    print "The calculated square root is ", x, " and the error is ", e

