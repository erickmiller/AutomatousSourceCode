
# Return True if the argument to the function
# is a sorted-in-ascending order tuple. DO NOT use builtin functions
# like sort/sorted etc to solve this.

def is_sorted(a):
  i=0
  for num in a:
    if i == a.index(a[-1]):
      return 1
    i=i+1
    if num > a[i]:
      return 0 
   

print'\n\n***************OUTPUT****************\n'
assert(is_sorted((10, 20, 30, 32, 33)))

assert(is_sorted((1,)))

assert(is_sorted((1,2)))

assert(not is_sorted((2, 1)))

assert(not is_sorted((1, 4, 7, 8, 6)))

assert(not is_sorted((10, 20, 30, 25, 34, 45, 67)))

print'\nAll conditions are verified..\n'
