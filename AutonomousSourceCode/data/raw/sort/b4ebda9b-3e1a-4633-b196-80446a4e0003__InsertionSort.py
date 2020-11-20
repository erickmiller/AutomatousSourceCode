__author__ = 'ingthor'

import random
# Insertion sort algorithm
# Insert any array
def InsertionSort(A):
    # input size
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while (i >= 0) and (A[i] > key):
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A


# returns array sorted

def InsertionSortAsc(A):
    # input size
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while (i >= 0) and (A[i] < key):
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A


# n is size of test

def Test(n, OrderFunc):
    testA = []
    for i in range(0, n):
        testA.append(random.randint(0, n))
    print("UnSorted")
    print(testA)
    sortedA = OrderFunc(testA)
    print("Sorted")
    print(sortedA)
    return
