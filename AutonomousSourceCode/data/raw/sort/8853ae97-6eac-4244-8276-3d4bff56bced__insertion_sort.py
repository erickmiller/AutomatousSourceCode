def insertion_sort(unsorted_list):
  sorted_list = []

  for idx1, val1 in enumerate(unsorted_list):
    current = unsorted_list[idx1]
    inserted = False
    
    if idx1 == 0:
      sorted_list.append(current)
    else:
      for idx2, val2 in enumerate(sorted_list):

        if val2 > val1 and not inserted:
          sorted_list.insert(idx2, val1)
          inserted = True
      if not inserted:
        sorted_list.append(val1)

  return sorted_list