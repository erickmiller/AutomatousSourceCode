# -*- coding: utf-8 -*-

import os
import sys

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while (left_index < len(left)) and (right_index < len(right)):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    if left:
        sorted_list.extend(left[left_index:])
    if right:
        sorted_list.extend(right[right_index:])

    return sorted_list

def merge_sort(l):
    if len(l) <= 1:
        return l
        
    mid = len(l) / 2
    left  = l[mid:]
    right = l[:mid]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

if __name__ == "__main__":
    from random import shuffle
    l = [1,2,3,4,5,6,7,8,9]
    shuffle(l)
    assert merge_sort(l) == [1,2,3,4,5,6,7,8,9]
