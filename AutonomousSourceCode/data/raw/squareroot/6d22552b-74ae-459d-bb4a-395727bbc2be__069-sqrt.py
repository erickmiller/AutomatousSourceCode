#!/usr/bin/python

# Implement int sqrt(int x).

# Compute and return the square root of x.

import sys

# Binary search in range from 1 to x / 2. O(log(n)).
def sqrt(x):
    if x == 0 or x == 1:
        return x
    i, j = 1, x / 2
    while i <= j:
        m = (i + j) / 2
        if m * m > x:
            j = m - 1
        elif m * m < x:
            i = m + 1
        else:
            return m
    return i - 1

def main():
    print sqrt(int(sys.argv[1]))

main()
