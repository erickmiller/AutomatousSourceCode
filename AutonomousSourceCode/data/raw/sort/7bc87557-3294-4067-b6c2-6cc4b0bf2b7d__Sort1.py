#!/bin/python
def insertionSort(ar):
    sorted = 0
    i = len(ar) - 2
    val = ar[len(ar)-1]
    while not sorted:
        if i < 0:
            ar[0] = val
            sorted = 1
        elif (ar[i] > val):
            ar[i+1] = ar[i]
            i -= 1
        else:
            ar[i+1] = val
            sorted = 1
        print str(ar).strip('[]').replace(",", "")
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)