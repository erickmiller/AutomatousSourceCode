#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math

def is_lucky(x):
    s = str(x)
    for c in s:
        if c != "4" and c != "7":
            return False
    return True

def is_almost_lucky(x):
    if is_lucky(x):
        return True
    square_root = int(math.sqrt(x)) + 1
    for i in range(1, square_root + 1):
        if x % i == 0 and (is_lucky(i) or is_lucky(x / i)):
            return True
    return False

n = int(sys.stdin.readline().strip())

if is_almost_lucky(n):
    print "YES"
else:
    print "NO"
