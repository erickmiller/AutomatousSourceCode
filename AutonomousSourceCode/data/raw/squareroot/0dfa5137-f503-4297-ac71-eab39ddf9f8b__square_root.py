def square_root(n, start=None, end=None):
  if start == None: start = 1
  if end == None: end = n
  mid = (end + start) / 2
  print (start, end, mid)
  squared_n = mid * mid
  if squared_n == n:
    return mid
  elif squared_n > n:
    return square_root(n, start, mid)
  elif squared_n < n:
    return square_root(n, mid, end)

print square_root(625)


