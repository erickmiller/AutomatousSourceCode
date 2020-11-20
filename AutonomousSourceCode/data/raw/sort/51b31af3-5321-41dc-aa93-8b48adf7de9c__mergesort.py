#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: mergesort.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Implementation of the mergesort algorithm.
Time complexity: O(nlogn)
"""


def merge(left, right, result):
    """This is just the merge algorithm for mergesort.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        result[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        result[k] = right[j]
        k += 1
        j += 1

    return result


def sort(seq):
    """Implementation of merge sort.
    Time complexity: O(nlogn)
    Space complexity: O(n)
    """

    if len(seq) <= 1:
        return seq

    mid = len(seq) // 2
    left = sort(seq[:mid])
    right = sort(seq[mid:])
    merge(left, right, seq)

    return seq


def test():
    import random

    A = [2, 2, 3, 4]
    B = [1, 2, 3, 5, 6]
    C = [None] * (len(A) + len(B))
    merge(A, B, C)
    assert C == [1, 2, 2, 2, 3, 3, 4, 5, 6]

    A = [-1, 3, 10, 10]
    B = [-5, -1, 5, 9, 11]
    C = [None] * (len(A) + len(B))
    C = merge(A, B, C)
    assert C == [-5, -1, -1, 3, 5, 9, 10, 10, 11]

    A = []
    B = [1, 2]
    C = [None] * (len(A) + len(B))
    C = merge(A, B, C)
    assert C == [1, 2]

    S = []
    S_sorted = sort(S)
    assert S_sorted == []

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

    S = range(10000)
    random.shuffle(S)
    S_sorted = sort(S)
    assert S_sorted == sorted(S)

    S = [random.randint(-1000, 1000) for _ in range(10000)]
    S_sorted = sort(S)
    assert S_sorted == sorted(S)


if __name__ == '__main__':
    test()
