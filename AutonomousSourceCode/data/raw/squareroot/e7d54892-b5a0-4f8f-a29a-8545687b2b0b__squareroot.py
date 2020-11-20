#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

# Support python2 
from __future__ import division

def sqrt(number):
    """This function uses division to converge to a square root"""

    # We have to initialize these variables
    guess = 2  # Our first guess will always be 2
    old = 0    # This must be set to something, or we get an error

    # This is a while loop, it repeats the block
    # until the test (guess != old) is False
    # This loop will converge towards the square root
    while (guess != old): 
        old = guess              # We need to keep a copy of our previous guess
        quotient = number/guess  
        guess = (quotient + guess)/2  # We average our guess and  quotient

    # Once we are done, we must return the value
    return guess

def main():
    print(sqrt(2685)) # Display the square root of 2685
    print(sqrt(2))    # Display the square root of 2
    #print(sqrt(-2))  # never converges


# This calls main
# This is specific to python
if __name__ == '__main__':
    main()
