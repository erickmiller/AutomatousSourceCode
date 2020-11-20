#!/usr/bin/env python
# -*- coding: utf-8 -*-

def testSort(lst):
    if lst: return testSort([elem for elem in lst[1:] if elem<lst[0]]) + lst[0:1] + testSort([elem for elem in lst[1:] if elem>=lst[0]])
    return []

func = testSort

lst = [1, 2, 33, 3, 4, 6, 7, 788, 9, 5, 33, 222]

sortedList = func(lst)
print sortedList