# -*- coding: utf-8 -*-

import random


def bubble_sort(alist):
    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(alist)-1):
            if alist[idx] > alist[idx+1]:
                alist[idx], alist[idx+1] = alist[idx+1], alist[idx]
                sorted = False
    return alist


def selection_sort(alist):
    for pos in range(len(alist)-1):
        min_pos = pos
        for idx in range(pos, len(alist)):
            if alist[min_pos] > alist[idx]:
                min_pos = idx
        alist[pos], alist[min_pos] = alist[min_pos], alist[pos]
    return alist


def heap_sort(alist):
    raise(NotImplementedError)


def insertion_sort(alist):
    raise(NotImplementedError)


def shell_sort(alist):
    raise(NotImplementedError)


def merge_sort(alist):
    raise(NotImplementedError)


def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    pivot = alist[0]
    greater = []
    lesser = []
    for element in alist:
        if element <= pivot:
            lesser.append(element)
        else:
            greater.append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

