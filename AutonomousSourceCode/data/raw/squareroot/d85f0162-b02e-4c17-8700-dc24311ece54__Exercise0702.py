"""
Exercise 7.2. 

if abs(y-x) < epsilon:
    break

Encapsulate this loop in a function called square_root that takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a.

"""
import math

def square_root(a):
    
    x = a / 3.0
    epsilon = 0.000000000001
    
    while abs(a - (x**2)) > epsilon:
        x = (x + a/x) / 2
    return x

print square_root(0)
