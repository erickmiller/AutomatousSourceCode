#!/usr/bin/env python
def sqrt(n):
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while better != approx:
        approx = better
        better = (approx + n/approx)/2.0
    return approx

if __name__ == '__main__':
    print 'The square root of two is approximately: ' + str(sqrt(2))
    print
