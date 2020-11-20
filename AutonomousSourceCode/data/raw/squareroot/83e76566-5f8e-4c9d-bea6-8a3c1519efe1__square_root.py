""" Comparing different ways of finding square root
1st column number a
2nd col square root from written function 
3rd col square root computed by math.sqrt
4th col absolute value of difference between the two estimates
"""

def findsquare(a):
    epsilon = 0.0000001
    x = a/2.0
    while True:
        y = (x + a/x) / 2.0
        if abs(y-x) < epsilon:
            return x
        x = y

def test_square(a):
    import math
    print a,
    print (10-len(str(a)))*' ',
    b = findsquare(a)
    print b,
    print (10-len(str(b)))*' ',
    c = math.sqrt(a)
    print c,
    print (10-len(str(c)))*' ',
    print abs(c - b)

test_square(35)
test_square(1001)
test_square(30000)
test_square(2)



