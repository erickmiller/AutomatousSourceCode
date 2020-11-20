from math import *

def square_root(a):
  epsilon = 0.0000001
  x = a/2.0
  while True:
    print x
    y = (x + a/x) / 2
    if abs(y-x) < epsilon:
      break
    x = y
  return x

print "Give me a number to calculate the square root of: ",
a = raw_input()
a = float(a)
print("The square root of %f is %f") % (a, square_root(a))

