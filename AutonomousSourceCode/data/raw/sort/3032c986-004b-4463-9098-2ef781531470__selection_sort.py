def selection_list_sort(xs):
  unsorted_l = xs
  sorted_l = []
  min_idx = 0

  while unsorted_l:
    for i in range(len(unsorted_l)):
      if unsorted_l[i] < unsorted_l[min_idx]:
        min_idx = i
    sorted_l.append(unsorted_l[min_idx])
    del unsorted_l[min_idx]
    min_idx = 0

  return sorted_l

def selection_dict_sort(d):
  unsorted = d
  sorted_l = []
  min_key_val = None, None

  while unsorted:
    for k in unsorted:
      if not min_key_val[0] or unsorted[k] < min_key_val[1]:
        min_key_val = k, unsorted[k]
    sorted_l.append(min_key_val)
    del unsorted[min_key_val[0]]
    min_key_val = None, None

  return sorted_l

l = [12,12,15,2,7,2,12]
print selection_list_sort(l)

d = {"the": 10, "and": 11, "hello": 15, "goodbye": 11}
print selection_dict_sort(d)
