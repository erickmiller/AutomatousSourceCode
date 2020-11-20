#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: quicksort.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Recursive implementation of quicksort
to sort an array A in place.
"""

import random

def partition(A, p, begin, end):
    """Partition the subarray A[begin:end] about the pivot p
    where begin <= p < end
    and return the new index of the pivot in the A."""
    pivot = A[p]
    left = begin  # Elements left of A[left] is <= pivot
    right = end - 2  # Elements right of A[right] > pivot
    A[p], A[end-1] = A[end-1], A[p]  # Swap pivot and last element in subarray

    while left < right:
        if A[left] <= pivot:
            left += 1
        else:
            A[left], A[right] = A[right], A[left]
            right -= 1

    # At this point, elements left of A[left] are <= pivot
    # elements right of A[right] > pivot
    # left == right
    if A[left] <= pivot:
        A[right + 1], A[end-1] = A[end-1], A[right + 1]
        return right + 1
    else:
        A[left], A[end-1] = A[end-1], A[left]
        return left


def pick_pivot(begin, end):
    """Return index of pivot which is a value in [begin, end)."""
    return random.randint(begin, end-1)  # Do not include endpoint.


def quicksort_helper(A, begin, end):
    if end - begin <= 1:  # 1 or less element to sort.
        return A

    p = pick_pivot(begin, end)  # Index of pivot.
    p = partition(A, p, begin, end)
    quicksort_helper(A, begin, p)  # Note p is not included in subarray to sort
    quicksort_helper(A, p+1, end)


def sort(A):
    """"Recursive implementation of Quicksort
    to sort an array A in place."""
    quicksort_helper(A, 0, len(A))
    return A


def test():
    S = []
    S_sorted = sort(S)
    assert S_sorted == []

    S = [-1]
    S_sorted = sort(S)
    assert S_sorted == [-1]

    S = [-1, -3]
    S_sorted = sort(S)
    assert S_sorted == [-3, -1]

    S = [2, 2, -1, -1, 3, 10, 100]
    S_sorted = sort(S)
    assert S_sorted == sorted(S)

    S = [2, 3, -1, 0, 5]
    S_sorted = sort(S)
    assert S_sorted == sorted(S)

    S = range(20)
    random.shuffle(S)
    S_sorted = sort(S)
    assert S_sorted == sorted(S)

    S = range(20)
    random.shuffle(S)
    S = [s if random.randint(0, 1) else -s for s in S]
    S_sorted = sort(S)
    assert S_sorted == sorted(S)

    S = range(10)
    S_sorted = sort(S)
    assert S_sorted == sorted(S)


if __name__ == '__main__':
    test()
