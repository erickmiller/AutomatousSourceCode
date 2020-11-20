#!/usr/bin/env python
#
# Author:	Felipe Pierin
# Author:	Viviane Bonadia

from compare import cmp

def quicksortCmp(c, toSort):
    if len(toSort) <= 1:
        return toSort
 
    end = len(toSort) - 1
    pivot = toSort[end]
 
    low = []
    high = []
 
    for num in toSort[:end]:
        if  cmp(c, num, pivot, (num <= pivot)):
            low.append(num)
        else:
            high.append(num)
 
    sortedList = quicksortCmp(c, low)
    sortedList.append(pivot)
    sortedList.extend(quicksortCmp(c, high))
    return sortedList 
		
def quicksort(A):
	c = []
	x = quicksortCmp(c, A)
	return c
