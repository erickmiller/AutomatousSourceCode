#!/usr/bin/env python

"""
Exam 2: SOLUTION                                                      /25

For syntax help see:

  /Code/Python/test.py 
  /Code/Python/functions.py 
  /Solutions/lab08/lab08.py

  Note: Leave existing code in - your job is to add the function definitions 
  as specified

  Do not call existing functions in the python math library - write your 
  funtions from scratch.
"""

from sys import argv

"""
#1. Write a recursive function exp_2 that takes as arguments integer x, x >= 0,
    and returns 2^x. 
"""

def exp_2( x ):               # f(x) = 2^x, for x >= 0
  if x == 0:
     return 1 
  else:
     return 2 * exp_2(x-1) 

print exp_2(5)                # call the function

"""
#2. Write a function log_2 that takes as arguments integer x, where x is some
    value 2^k, k >= 0, and returns log base 2 of x. 
"""

def log_2( x ):               # g(x) = log_base_2(x), for x = 2^k, k >= 0
  if x == 1:
     return 0
  else:
     return 1 + log_2( x/2.0) 

print log_2(32)               # call the function

"""
#3. Write a function sq_rt that takes as arguments an integer x, where x is 
    some integer k*k, k >= 1, and returns the square root of x. 
"""

def sq_rt( x ):               # f(x) =  square_root(x), for x = k*k, k >= 1  
   tmp = 1
   while tmp < x / 2:
      if tmp * tmp == x:
         return tmp
      else:
         tmp = tmp + 1
   return 0

print sq_rt(25)               # call the function

def sq_rt2( x ):              # another version
   tmp = 1
   while x/tmp != tmp:
      tmp = tmp + 1
   return tmp

# print sq_rt2(25)              # call the function
"""
#4. Write a function square that takes as arguments integer x, x >= 1, and 
    returns x*x. 
"""
 
def square( x ):               # g(x) =  x*x, for x >= 1  
  return x * x

print square(5)                # call the function

"""
#5. Write a function inverse that takes as arguments two functions f and g and 
    an integer x, x >= 1. Function inverse returns true if f(g(x)) == x. 
"""

def inverse (f, g, x):           # return true if f(g(x)) = x
  return (f (g (x) ) == x)

print inverse(log_2, exp_2, 5)                  # should return true
print inverse(sq_rt, square, 5 )                # should return true
print inverse(lambda x: x*2, lambda x: x+2, 5)  # should return false
