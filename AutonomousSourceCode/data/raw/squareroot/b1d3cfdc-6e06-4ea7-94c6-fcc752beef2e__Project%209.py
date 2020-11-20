""" using Newton's Method as a means of finding progressively more accurate roots of any real function
"""
from math import sqrt

error = 0.000001
number_of_iterations = 0

# Returns how far 'x' is from the square root of 'a' and the number
# of times iterated through to reach our margin of error.
def square_root(a, x):
    a = float(a)
    next_x = float(x + (a/x))/2
    global number_of_iterations
    number_of_iterations += 1

    if abs(next_x - sqrt(a)) < error:
        print "Number of iterations: %s" % number_of_iterations
        return float(next_x)
    else:
        return square_root(a, next_x)

# print square_root(10, 5)
print square_root(10, 3)













