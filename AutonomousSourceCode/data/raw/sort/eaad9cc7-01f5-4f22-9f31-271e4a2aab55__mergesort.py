def merge_sort(arr):

  if len(arr) > 1:
    middle = len(arr) / 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)
  else:
    return arr

def merge(left, right):
  sorted_arr = []

  while len(left) and len(right):
    if left[0] <= right[0]:
      sorted_arr.append(left[0])
      left = left[1:]
    else:
      sorted_arr.append(right[0])
      right = right[1:]

  if len(right):
    sorted_arr += right
  if len(left):
    sorted_arr += left
  return sorted_arr

        


