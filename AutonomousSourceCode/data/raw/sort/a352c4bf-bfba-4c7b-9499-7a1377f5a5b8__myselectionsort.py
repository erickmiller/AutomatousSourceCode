"""
Selection Sort
"""
import sys

def selection_sort(lst):
  l = lst[:]
  sorted = []
  while len(l):
    lowest = l[0]
    for x in l:
      if x < lowest:
        lowest = x
    sorted.append(lowest)
    l.remove(lowest)
  return sorted
