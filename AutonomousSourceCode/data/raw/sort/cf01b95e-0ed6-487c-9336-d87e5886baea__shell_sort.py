#!/usr/bin/env python
'''
note: really fast on mostly sorted arrays
'''


import random


def insertion_sort(arr, h=1):
  '''  '''
  for i in range(h, len(arr)):
    j = i
    while j >= h and arr[j-h] > arr[j]:
      swap = arr[j-h]
      arr[j-h] = arr[j]
      arr[j] = swap
      j -= h
  return arr


def shell_sort(arr):
  ''' h-sort the array, decrement h, and repeat untill the array has been 1 sorted '''
  # initialize the first gap value
  h = 1
  while h < len(arr)/3:
    h = 3*h + 1
  # repeatedly h-sort the array
  while h >= 1:
    insertion_sort(arr, h=h)
    # update the gap
    h = h/3
  return arr


def test():

  
  for i in range(10):
    test_values = tuple(random.randrange(1000) for i in range(100))
    test_sorted = tuple(sorted(test_values))

    assert test_sorted == tuple(shell_sort(list(test_values)))


  pass

if __name__ == '__main__':
  test()

