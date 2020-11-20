#! /usr/bin/python

import math

def insertionSortInt(toSort, numberMask=0xFFFFFFFF):
    n = len(toSort)
    for j in range(2,n):
        key = toSort[j]
        i = j - 1
        while i > 0 and (toSort[i] & numberMask) > (key & numberMask):
            toSort[i + 1] = toSort[i]
            i = i - 1
        toSort[i + 1] = key
    return toSort

def bucketSort(toSort):
    sortedOut = []
    return sortedOut

def radixSort(toSort, nbuckets=16):
    sortedOut = []
    groupBitsCount = math.log(nbuckets, 2)
    for i in range(nbuckets):
        pass
    return sortedOut

if __name__ == "__main__":
    print("[DEMO] - RadixSort.py")
    print(insertionSortInt([4, 5, 3, 16]))
