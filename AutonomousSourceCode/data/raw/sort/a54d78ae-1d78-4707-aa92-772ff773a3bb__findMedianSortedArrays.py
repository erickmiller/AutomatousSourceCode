#!/usr/bin/python
import math

def findMedianSortedArrays(A, B):
    le = len(A) + len(B)
    C = []
    for i in A:
        C.append(i)
    for i in B:
        C.append(i)
    C.sort()
    if le%2 == 1:
        return C[le/2]
    else:
        return (C[le/2]+C[le/2-1])/2.0


A = [1,2,3,4]
B = [56,7]
print findMedianSortedArrays(A,B)
