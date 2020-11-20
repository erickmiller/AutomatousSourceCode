##
# classic merge sort
# assumptions:
#   1. required order: ascending
#   2. input arrays are sorted (ascending)
##

def merge_sort(a, b):
  if not a: return b
  if not b: return a
  if a[0] > b[0]: return [b[0]] + merge_sort(a, b[1:])
  else:           return [a[0]] + merge_sort(a[1:], b)

if __name__ == '__main__':
  a = [1, 3, 5, 7, 9]
  b = [2, 4, 6, 8, 10]
  print merge_sort(a, b)

