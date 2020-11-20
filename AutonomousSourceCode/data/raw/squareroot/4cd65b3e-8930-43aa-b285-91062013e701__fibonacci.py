# Utilities related to the Fibonacci sequence, to be reused among problems

from math import sqrt

def fibonacci_generator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

# Returns the nth term of the Fibonacci sequence
def fibonacci_term(n):
    square_root_of_five = sqrt(5)
    phi = (1 + square_root_of_five)/2
    phi_2 = (1 - square_root_of_five)/2
    return int((phi**n - phi_2**n) / square_root_of_five)
