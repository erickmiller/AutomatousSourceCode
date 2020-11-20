"""
Exercise 7.3. 

To test the square root algorithm in this chapter, you could compare it with
math.sqrt. Write a function named test_square_root that prints a table like this:

1.0     1.0             1.0             0.0
2.0     1.41421356237   1.41421356237   2.22044604925e-16
3.0     1.73205080757   1.73205080757   0.0
4.0     2.0             2.0             0.0
5.0     2.2360679775    2.2360679775    0.0
6.0     2.44948974278   2.44948974278   0.0
7.0     2.64575131106   2.64575131106   0.0
8.0     2.82842712475   2.82842712475   4.4408920985e-16
9.0     3.0             3.0             0.0

The first column is a number, a; 
the second column is the square root of a, computed with the function from Section 7.5; 
the third column is the square root computed by math.sqrt; 
the fourth column is the absolute value of the difference between the two estimates.
"""
import math

def square_root(a):
    x = a / 3.0
    epsilon = 0.000000000001
    while abs(a - (x**2)) > epsilon:
        x = (x + a/x) / 2
    return x
    
def test_square_root(b):
    for i in range (1, b):
        print "%g\t\t%g\t\t\t%g\t\t%g" % (float(i), square_root(i), math.sqrt(i), (square_root(i) - math.sqrt(i)))
        
test_square_root(10)
        