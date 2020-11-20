#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 173
#
# Using up to one million tiles how many different "hollow" square
# laminae can be formed?
#
# We shall define a square lamina to be a square outline with a square
# "hole" so that the shape possesses vertical and horizontal
# symmetry. For example, using exactly thirty-two square tiles we can
# form two different square laminae:
#
#     * * * * * *    * * * * * * * * *
#     * * * * * *    * . . . . . . . *
#     * * . . * *    * . . . . . . . *
#     * * . . * *    * . . . . . . . *
#     * * * * * *    * . . . . . . . *
#     * * * * * *    * . . . . . . . *
#                    * . . . . . . . *
#                    * . . . . . . . *
#                    * * * * * * * * *
#
# With one-hundred tiles, and not necessarily using all of the tiles
# at one time, it is possible to form forty-one different square
# laminae.
#
# Using up to one million tiles how many different square laminae can
# be formed?
#
# Solved 11/13/10
# 132 problems solved
# Position #373 on level 3

import time
import sys
import math

start_time = time.clock()

TILES = 1000000

def odd(n):
    if ((n % 2) == 1): return True
    else:              return False

def even(n):
    if ((n % 2) == 0): return True
    else:              return False

def int_sqrt(n):
    # return the integer square root of an integer
    ans = int(n**.5)
    if   ((ans**2) == n): return ans
    elif ((ans**2) <  n): return ans+1
    elif ((ans**2) >  n): return ans


max_o = (TILES/4)+1
ans = 0

for o in range(3, max_o+1):
    max_i = o-2

    # TILES >= o**2 - i**2
    # => i**2 >= o**2 - TILES
    inner_size = o**2 - TILES
    if (inner_size <= 0):
        min_i = 1
    else:
        min_i = int_sqrt(inner_size)
    if   (odd(max_i) & even(min_i)):  min_i += 1
    elif (even(max_i) & odd(min_i)):  min_i += 1

    ans += 1 + (max_i - min_i)/2
    #print "Outer = {0}: min_i = {1}, max_i = {2}, solutions = {3}".format(o, min_i, max_i, (1 + (max_i - min_i)/2))
    #for i in range(min_i,max_i+1,2):
    #    print "    Outer = {0}, inner = {1}, tiles used = {2}".format(o,i, (o**2-i**2))

print "With TILES =", TILES, "Answer =", ans
print "Time taken =", time.clock() - start_time, "seconds"
sys.exit()
