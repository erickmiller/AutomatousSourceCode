import math
import random

# self-mad #
############

def my_own_assert(cond):
  if not cond:
    raise AssertionError
    
#my_own_assert(2 + 2 == 5)


# built in #
############
#assert(2+2 == 5)


# Precondtion and Postconditon #
################################
def square_root(x, eps= 10e-7):
  # PREcondition
  assert x >= 0     
  y = math.sqrt(x)
  # POSTcondition
  #assert y*y == x   
  assert abs((y*y)-x) < eps   # includes rounding error             
  return y


for i in range(1,1000):
  r = random.random() * 10000
  try:
    z = square_root(r)
  except:
    print r, r - math.sqrt(r) * math.sqrt(r) # Rounding Error!
    break
  
print "Done!"
