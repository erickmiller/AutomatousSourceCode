'''
Created on Oct 15, 2014

@author: Ben Athiwaratkun (pa338)

'''
#from __future__ import division
#import numpy as np


def sortedToAlternateSort(A):
    n = len(A)
    B = [None]*n
    # assume that A is sorted
    
    half = len(A)/2
    for i in range(half):
        B[2*i] = A[i]
        B[2*i+1] = A[n-1-i]
    if n % 2 == 1:
        B[n-1] = A[half]
    # take care of odd length case
    return B


def main():
    A = [1,5,2,5,6,8,2,3,7,2,0]
    B = sorted(A)
    print B
    print sortedToAlternateSort(B)
    print sortedToAlternateSort([1,2,3,4,5,6])
    print sortedToAlternateSort([1,2,3,4,5,6,7])
    
if __name__ == "__main__":
    main()