# Square root digital expansion
# Problem 80

# It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

# The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

from decimal import *
from math import *

def solve():
    return sum(list(map(digsum, range(2,100))))
    
    
def digsum(a):
    sum = 0
    if round(sqrt(a))**2 == a:
        return 0
    getcontext().prec = 110
    d = Decimal(a).sqrt()
    while d > 1:
        d = d / 10
    for i in range(0,100):
        d = d * 10
        sum += int(d) % 10
    return sum