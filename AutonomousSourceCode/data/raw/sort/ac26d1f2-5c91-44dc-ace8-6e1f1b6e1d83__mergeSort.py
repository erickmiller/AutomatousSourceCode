import math
import random

# Sort two integers
def sort_tuple(a, b):
  if a < b:
    return [a, b]
  else:
    return [b, a]

# Take two arrays and return merged array
# a and b should both be sorted arrays
def merge_sorted_arrays(a, b):
  # Index for a
  i = 0
  # Index for b
  j = 0
  # Create a new array to push values into and for final answer
  c = []
  # If there are still items in both a and b
  while i < len(a) or j < len(b):
    if i < len(a) and j < len(b):
      # If the thing in a is less than the thing in b
      if a[i] < b[j]:
        c.append(a[i])
        i += 1
      else:
        c.append(b[j])
        j += 1
    # If there are still items in a
    elif i < len(a):
      # Append the rest of a
      c.extend(a[i:len(a)])
      i = len(a)
    elif j < len(b):
      # Append the rest of b
      c.extend(b[j:len(b)])
      j = len(b)
  return c

# take an array, split it in half, sort each half and merge the result
def merge_sort(array):
  # split array in half:
  a = array
  halfway = int(math.ceil(len(a)/2.0))
  # first half, inclusive
  b = a[0:halfway]
  # second half, exclusive
  c = a[halfway:len(a)]
  # 
  # sort each half
  b_sorted = []
  c_sorted = []
  if len(b) > 2:
    b_sorted = merge_sort(b)
  elif len(b) == 2:
    b_sorted = sort_tuple(*b)
  else:
    b_sorted = b
  if len(c) > 2:
    c_sorted = merge_sort(c)
  elif len(c) == 2:
    c_sorted = sort_tuple(*c)
  else:
    c_sorted = c
  # merge the result
  return merge_sorted_arrays(b_sorted, c_sorted)


# 
A = []

for _ in range(101): A.append(random.randint(0,100))

A

merge_sort(A)
