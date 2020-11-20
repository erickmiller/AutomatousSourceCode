#!/bin/usr/python
import random

def unsorted(N):
    return [random.randrange(0, N*10) for r in xrange(N)]

def sort(L):
    sortedL = [L[0]]
    N = len(L)
    for i in xrange(1, N):
        si = len(sortedL) - 1
        while si >= 0 and L[i] < sortedL[si]:
            si -= 1
        if si == len(sortedL) - 1:
            sortedL.append(L[i])
            continue
        temp = sortedL[si+1:]
        sortedL[si+1] = L[i]
        sortedL[si+2:] = temp
    return sortedL

# from wiki
def insertion_sort(L):
    if len(L) == 1:
        return L
    b = insertion_sort(L[1:])
    m = len(b)
    for i in range(m):
        if L[0] <= b[i]:
            return b[:i]+[L[0]]+b[i:]
    return b + [L[0]]

if __name__ == '__main__':
    l = unsorted(10)
    print l
    print sort(l)
    print insertion_sort(l)
