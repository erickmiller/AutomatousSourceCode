#!/bin/python

def squareRootBi(x, epsilon):  
  assert epsilon > 0, 'epsilon must be postive, not ' + str(epsilon) 
  low = 0 
  high = max(x, 1) 
  guess = (low + high)/2.0 
  ctr = 1 
  while abs(guess ** 2 - x) > epsilon: 
    #print 'low:', low, 'high:', high, 'guess:', guess
    if guess**2 < x: 
      low = guess 
    else: 
      high = guess 
    guess = (low + high) / 2.0 
    ctr += 1 
    assert ctr <= 1000, 'iteration count exceeded' 
  print 'iterations:', ctr, 'Estimate:', guess 
  return guess
 
x = int(raw_input('Enter a value for x: '))
epsilon = float(raw_input('Enter an epsilon value (accuracy): '))
print squareRootBi(x, epsilon)

# this program will attempt to find the square root of a number, using binary search
