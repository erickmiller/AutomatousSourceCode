import sys
import math

def square_root(a):
    x = a/2.0
    y = x
    while True:
        #print "x = ", x
        y = (x + a / x) / 2.0
        #print "y = ", y
        if abs(y-x) < sys.float_info.epsilon:
            break

        x = y

    return x

def test_square_root():
    for i in range(1, 10):
        print i,
        mysqrt = square_root(i)
        print mysqrt,
        mathsqrt = math.sqrt(i)
        print mathsqrt,
        print abs(mysqrt - mathsqrt)

#test_square_root()

def factorial(n):
    if n < 0:
        return None
    elif n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def estimate_pi():
    tot = 0
    k = 0
    factor = (2 * math.sqrt(2)) / 9801

    while True:
        num = factorial(4 * k) * (1103 + (26390 * k))
        den = (factorial(k) ** 4) * (396 ** (4 * k))
        term = factor * (num / den)
        tot += term

        if abs(term) < 1e-15: break

        k += 1

    return 1 / tot

print estimate_pi()