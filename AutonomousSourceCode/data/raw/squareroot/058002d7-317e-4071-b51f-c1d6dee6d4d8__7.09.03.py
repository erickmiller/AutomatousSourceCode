"""To test the square root algorithm in this chapter, you could compare
it with math.sqrt. Write a function named test_square_root that prints a table.

The first column is a number, a; the second column is the square root of a
computed with the function from Section 7.5; the third column is the square root
computed by math.sqrt; the fourth column is the absolute value of the difference
between the two estimates."""


import math

def square_root(a):
    a = float(a)
    x = a/2
    while True:
        y = (x + a/x) / 2
        if x == y:
            break
        x = y
    return x

def square_root_table(n_range):
    for num in range(1, n_range):
        print num,
        print square_root(num),
        print math.sqrt(num),
        print abs(square_root(num) - math.sqrt(num))