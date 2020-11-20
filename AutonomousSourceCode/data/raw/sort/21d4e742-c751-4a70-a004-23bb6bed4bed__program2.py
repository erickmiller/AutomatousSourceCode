
# Return True if the argument to the function
# is a sorted-in-ascending order tuple. DO NOT use builtin functions
# like sort/sorted etc to solve this.

def is_sorted(a):
  b = len(a)
  if b == 1 :
    return 1
  for i in range(b-1):
    if a[i] > a[i+1] :
      return 0 
  return 1 
      



assert(is_sorted((10, 20, 30, 32, 33)))

assert(is_sorted((1,)))

assert(is_sorted((1,2)))

assert(not is_sorted((2, 1)))

assert(not is_sorted((1, 4, 7, 8, 6)))

assert(not is_sorted((10, 20, 30, 25, 34, 45, 67)))


