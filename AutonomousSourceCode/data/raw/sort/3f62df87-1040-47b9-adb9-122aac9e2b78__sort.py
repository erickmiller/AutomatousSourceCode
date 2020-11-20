import data_structures

def buble_sort(l):
  """Original list is sorted.
  """
  for i in range(len(l)):
    for j in range(i+1, len(l)):
      if (l[j-1]>l[j]):
        l[j-1], l[j] = l[j], l[j-1]

def insertion_sort(l):
  raise NotImplementedError()

def selection_sort(l):
  raise NotImplementedError()

def heap_sort(l):
  """Returns a sorted list. Original list is not modified.
  """
  h = SMinHeap()
  for el in l:
    h.push(el)
  sorted_list = [h.pop() for x in range(len(h.array))]
  return sorted_list

def quick_sort(l):
  """Returns a sorted list. Original list is not modified.
  """
  if len(l) == 1 or len(l) == 0:
    return l
  pivot = random.choice(l)
  return qsort([x for x in l if x < pivot]) + [pivot] + qsort([x for x in l if x > pivot])

def merge_sort(l, start, end):
  """Original list is sorted.
  """
  if (end-start < 2):
    return;
  middle = (start+end)//2

  def merge():
    nonlocal l, start, middle, end
    res = []
    rlen = end - start
    i, j, k = start, middle, 0
    while k<rlen:
      if i!=middle and (j==end or l[i]<=l[j]):
        res.append(l[i])
        i = i + 1
      elif j!=end and (i==middle or l[i]>l[j]):
        res.append(l[j])
        j = j + 1
      k = k + 1
    l[start:end] = res[:]

  mergesort(l, start, middle)
  mergesort(l, middle, end)
  merge(l, start, middle, end)
