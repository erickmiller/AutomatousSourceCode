import random

class ListSorter():
  """docstring for BubbleSort"""
  def __init__(self):
    pass
    
  def RecursiveBubbleSortMin(self, l):
    """docstring for sort"""
    # bubble up, find the least element and save it
    # recursive stoping point
    if len(l) == 1:
      return (l, 0)
    # bubble down min element
    algorithm_complexity = 0
    for i in range(1, len(l)):
      if l[0] > l[i]:
        l[0], l[i] = l[i], l[0]
      algorithm_complexity += 2
    # remember min
    l_min = l[:1]
    # recursively sort smaller list
    (smaller_l, recursive_complexity) = self.RecursiveBubbleSortMin(l[1:])
    # combine min and sorted smaller list
    return (l_min + smaller_l, algorithm_complexity + recursive_complexity)

  def RecursiveBubbleSortMax(self, l):
    """docstring for sort"""
    # bubble up, find the greatest element and save it
    # recursive stoping point
    if len(l) == 1:
      return (l, 0)
    # bubble up max element
    algorithm_complexity = 0
    current_max_i = 0
    for i in range(1, len(l)):
      if l[current_max_i] > l[i]:
        l[current_max_i], l[i] = l[i], l[current_max_i]
      current_max_i = i
      algorithm_complexity +=2
    # remember max
    l_max = l[-1:]
    # recursively sort smaller list
    (smaller_l, recursive_complexity) = self.RecursiveBubbleSortMax(l[:-1])
    # combine sorted smaller list and max
    return (smaller_l + l_max, algorithm_complexity + recursive_complexity)

  def BubbleSort(self, l2):
    """docstring for sort2"""
    # bubble down, find the smallest element and put into the ith position
    algorithm_complexity = 0
    l = l2[:]
    for i in range(len(l)):
      for j in range(i, len(l)):
        if l[i] > l[j]:
          l[i], l[j] = l[j], l[i]
        algorithm_complexity += 2
    return l, algorithm_complexity

  def RecursiveMergeSort(self, l):
    """docstring for sort2"""
    # recursive stopping point
    if len(l) == 1:
      return (l, 0)

    # divide task in smaller subtasks
    half_size = len(l)/2
    l1 = l[:half_size]
    l2 = l[half_size:]
    # and recursively sort them
    l1_sorted, l1_complexity = self.RecursiveMergeSort(l1)
    l2_sorted, l2_complexity = self.RecursiveMergeSort(l2)

    # merge results
    algorithm_complexity = 0
    l_sorted = []
    x = 0
    y = 0
    while True:
      algorithm_complexity += 2
      if l1_sorted[x] < l2_sorted[y]:
        l_sorted.append(l1_sorted[x])
        x += 1
        if x >= len(l1_sorted):
          l_sorted += l2_sorted[y:]
          break
      else:
        l_sorted.append(l2_sorted[y])
        y += 1
        if y >= len(l2_sorted):
          l_sorted += l1_sorted[x:]
          break
    return (l_sorted, algorithm_complexity + l1_complexity + l2_complexity)

  def RecursiveRandomSort(self, l):
    # Recursive stopping point
    if len(l) == 1:
      return (l, 0)

    # Divide task into random number subtasks
    division = random.randint(1, len(l)-1)
    l1 = l[:division]
    l2 = l[division:]
    
    l1_sorted, l1_complexity = self.RecursiveRandomSort(l1)
    l2_sorted, l2_complexity = self.RecursiveRandomSort(l2)

    # merge results
    algorithm_complexity = 0
    l_sorted = []
    x = 0
    y = 0
    while True:
      algorithm_complexity += 2
      if l1_sorted[x] < l2_sorted[y]:
        l_sorted.append(l1_sorted[x])
        x += 1
        if x >= len(l1_sorted):
          l_sorted += l2_sorted[y:]
          break
      else:
        l_sorted.append(l2_sorted[y])
        y += 1
        if y >= len(l2_sorted):
          l_sorted += l1_sorted[x:]
          break
    return (l_sorted, algorithm_complexity + l1_complexity + l2_complexity)
  
  def InsertionSort(self, l):
    algorithm_complexity = 0
    for i in range(len(l)):
      val = l[i]
      # j is the element before i which i will be compared to
      j = i - 1
      while j >= 0 and val < l[j]:
        # If the value is less than j, change j's index to the value's,
        # switching their spots.
        # Pick the next j value which is one less than the previous j.
        algorithm_complexity += 2
        l[j + 1] = l[j]
        j -= 1
      # When the value is greater than j, return its position to be just after j
      l[j + 1] = val
    return l, algorithm_complexity

  def RecursiveInsertionSort(self, unsorted_list):
    sorted_list = unsorted_list[:1]
    algorithm_complexity = self.__RecursiveInsertionSort(sorted_list,
                                                         unsorted_list[1:])
    return (sorted_list, algorithm_complexity)
    
  def __RecursiveInsertionSort(self, sorted_list, unsorted_list):
    algorithm_complexity = 0
    
    if not unsorted_list:
      return algorithm_complexity
    current = unsorted_list[0]
    algorithm_complexity += 2
    
    j = len(sorted_list) - 1
    sorted_list.append(current)
    while j >= 0 and current < sorted_list[j]:
      # If the value is less than j, change j's index to the value's,
      # switching their spots.
      # Pick the next j value which is one less than the previous j.
      sorted_list[j + 1] = sorted_list[j]
      algorithm_complexity += 2
      j -= 1
    sorted_list[j + 1] = current
    
    algorithm_complexity += self.__RecursiveInsertionSort(sorted_list,
                                                          unsorted_list[1:])
    return algorithm_complexity
  
  # Returns (sorted list, complexity)
  def RecursiveQuicksort(self, l):
    algorithm_complexity = 0
    if len(l) <= 1:
      return l, algorithm_complexity
    pivot_idx = random.randint(0, len(l) - 1)
    less = []
    greater = []
    for i in l:
      if i <= l[pivot_idx]:
        less.append(i)
      else:
        greater.append(i)
      algorithm_complexity += 2
    l_less, a = self.RecursiveQuicksort(less)
    l_greater, b = self.RecursiveQuicksort(greater)
    
    return l_less + l_greater, (algorithm_complexity + a + b)
