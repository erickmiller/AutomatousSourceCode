'''Sort a given array using mergesort algorithm'''

import copy

COUNT_INVERSIONS = 0

def merge(a, b):
    '''Given two arrays a and b return a sorted array'''
    i = j = 0
    sorted_array = []
    while i < len(a) and j <len(b):
        if a[i] < b[j]:
            sorted_array.append(a[i])
            i = i+1
        else:
            sorted_array.append(b[j])
            j = j+1

    sorted_array.extend(a[i:])
    sorted_array.extend(b[j:])
    return sorted_array

def mergesort(a):
    if not len(a)>1:
        return a

    middle = int(len(a)/2)
    left = mergesort(a[:middle])
    right = mergesort(a[middle:])

    return merge(left, right)

