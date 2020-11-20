#!/usr/bin/python

#============================================================================
# Project Euler: http://wwww.projecteuler.net
# Problem 10:
# Find the sum of all the primes below two million
#     - modification of euler7
#============================================================================

#import libraries/modules
import sys
from math import sqrt, floor
import time

#constants
LIMIT = 2000000

#find square root of passed number
def squareRoot(x):
     root = int(floor(sqrt(x)))
     #make the root number odd
     if root % 2 == 0:
          root +=1
     return root

#checks to see if number is prime
def checkPrime(x):
     prime = True   #flag
     
     #basic simple check to see if number passed is even, if it is then it's not a prime number
     if x % 2 == 0: 
          return False
     
     checkedNumber = squareRoot(x)
     for i in range(3,checkedNumber+2,2):
          if x % i == 0:
               prime = False
               break
     return prime

count = 0
sum = 2
count = 3
t0 = time.clock()
#main 
while count < LIMIT:
     if checkPrime(count):
          print count
          sum += count
     count += 2
t1 = time.clock() - t0

#total time is:  13.1200178791
print "sum of primes below", LIMIT, "is", sum
print "total time is: ", t1