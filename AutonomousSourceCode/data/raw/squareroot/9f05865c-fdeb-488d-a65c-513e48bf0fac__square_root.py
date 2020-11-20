"""
square root using while
(c) @brupoon
Ch. 7, ex. 3 Thinkpython
"""

from math import sqrt
from prettytable import PrettyTable

def square_root(a):
    """Approximates the square root of input a to accuracy of 0.000001"""
    x = a/2
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < 0.000001:
            break
        x = y
        
    return x

def test_square_root():
    """ Tests square_root against math.sqrt for int vals from 1-9 inclusive"""
    mytab = PrettyTable(["number", "est Sqrt", "math Sqrt", "abs diff"])
    mytab.padding_width = 1
    for x in range(1,10):
        math_val = sqrt(x)
        bp_val = square_root(x)
        difference = math_val - bp_val
        if difference < 0:
            difference = -difference
            #ghetto abs()
        mytab.add_row([x,math_val,bp_val,difference])
    print(mytab)

if __name__ == '__main__':
    test_square_root()