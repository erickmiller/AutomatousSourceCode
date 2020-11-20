import math

def square_root(a,x):
    y = (x + a/x) / 2
    return y

def math_squrt(a,x):
     m = math.sqrt(a)
     return m

def test_square_root(a,x):
     m = math_squrt(a,x)
     y = square_root(a,x)
     c = m - y 
     print a ,'		',  m ,'		', y,'		', c


test_square_root(2,3)
