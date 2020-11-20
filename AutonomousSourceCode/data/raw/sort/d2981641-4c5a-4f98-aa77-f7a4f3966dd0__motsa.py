#!/usr/bin/env python
import math
def findMedianSortedArrays(A, B):
    A.extend(B)
    A.sort()
    n = len(A)
    i1, i2 = int(math.floor((n-1)/2.0)), int(math.floor(n/2.0))
    return (A[i1] + A[i2]) / 2.0
