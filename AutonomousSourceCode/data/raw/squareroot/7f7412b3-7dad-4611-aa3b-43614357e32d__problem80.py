# Project Euler problem 80
# cf. http://d.hatena.ne.jp/inamori/20100216/p1

from decimal import Decimal, getcontext
from projecteuler import cntfrac_sqrt, flatten, squares_below, time_func
from itertools import repeat, dropwhile, count
from math import sqrt


def cntfrac2float(fractions):
    """Calculate continued fraction and return a float type number.
    arrange the projecteuler.cntfrac2float"""
    getcontext().prec = 101
    f = Decimal("0.0")
    n = len(fractions)-1
    while n > 0:
        f = Decimal("1.0") / (fractions[n] + f)
        #print f
        n -= 1
    return f + fractions[0]

def sum_digits(numbers):
    """Return the sum of the first one hundred decimal digits
    for all the irrational square root."""
    numbers = list(str(numbers))
    numbers.remove(".")
    numbers = numbers[:100]
    return sum([int(x) for x in numbers])

def create_cntfrac(fraction):
    new_frac = [[fraction[0]]]
    for i in repeat(fraction[1:], 200/len(fraction[1:])):
        new_frac.append(i)
    new_frac = flatten(new_frac)
    return new_frac

def main1():
    """answer is wrong."""
    answer = 0
    squares = squares_below(101)
    for i in range(1, 101):
        if i in squares:
            #print int(sqrt(i))
            pass
        else:
            fractions = create_cntfrac(cntfrac_sqrt(i))
            num = cntfrac2float(fractions)
            #print num
            #print sum_digits(num)
            answer += sum_digits(num)
    #answer += 55
    print answer

def head(a):
    for e in a:
        return e

def take(n, a):
    counter = 0
    for e in a:
        yield e
        counter += 1
        if counter == n:
            break

def gen_digits(n):
    while n:
        yield n % 10
        n /= 10

def square_root(n, l, m = 0):
    if l == 0:
        return m
    
    d = head(dropwhile(lambda d: d * (d + 20 * m) <= n, count(1))) - 1
    n -= d * (d + 20 * m)
    m = m * 10 + d
    return square_root(n * 100, l - 1, m)

def main2():
    N = 100
    M = 100
    print sum(map(lambda n: sum(gen_digits(square_root(n, M))),
            filter(lambda n: square_root(n, 1) ** 2 != n, range(1, N + 1))))

if __name__ == '__main__':
    time_func(main2)
