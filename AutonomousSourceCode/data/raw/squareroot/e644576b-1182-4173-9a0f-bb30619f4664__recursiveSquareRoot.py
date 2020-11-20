# Finds the square root of a number using recursion 


def rec_square_root(x, epsilon=0.01, low=None, high=None):

  if low == None:
    low = 0.0 
  if high == None:
    high = x
  bisection = (low+high)/2.0


  if abs(bisection**2 - x) < epsilon or bisection > x:
    return bisection

  else:
    if bisection**2 < x:
      return rec_square_root(x, epsilon, bisection, high)
    else:
      return rec_square_root(x, epsilon, low, bisection)

print rec_square_root(4)
print rec_square_root(16)
print rec_square_root(98)