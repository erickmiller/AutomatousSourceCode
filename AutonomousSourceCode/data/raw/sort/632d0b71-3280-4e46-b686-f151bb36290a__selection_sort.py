# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:46:19 2013

@author: lars
"""

def exch(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    
# -----------------------------------------------------------------------------

# Selection sort
       
def sort(lst):
    sorted_end_idx = 0
    while sorted_end_idx < len(lst):
        smallest_idx = sorted_end_idx
        i = sorted_end_idx
        while sorted_end_idx < len(lst):
            if lst[i] < lst[smallest_idx]:
                smallest_idx = i
            i+=1
        exch(lst, sorted_end_idx, smallest_idx)
        sorted_end_idx += 1
    return lst

