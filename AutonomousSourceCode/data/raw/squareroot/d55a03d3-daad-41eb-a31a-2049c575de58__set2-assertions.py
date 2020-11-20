#!/usr/bin/env python
# Random testing with assertion for pre and post conditions
import math
import random

def my_square_root(x):
    assert x >= 0
    y = math.sqrt(x)
    try:
        assert y * y == x
    except AssertionError, e:
        print x, y, y * y
        raise Exception
    return y

for i in xrange(1000):
    r = int(random.random() * 10000)
    z = my_square_root(r)

print "Done!"