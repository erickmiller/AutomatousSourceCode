#!/usr/bin/env python

import itertools
import math
import unittest

def divisible_by(dividend, divisor):
    return dividend % divisor == 0

def is_even(n):
    return divisible_by(n, 2)

def take_while_less_than(n, xs):
    def less_than_n(x):
        return x < n
    return itertools.takewhile(less_than_n, xs)

def take_while_less_than_or_equal(n, xs):
    def less_than_or_equal_to_n(x):
        return x <= n

    return itertools.takewhile(less_than_or_equal_to_n, xs)

def fibonacci():
    previous = 1
    current = 1

    while True:
        yield current
        temporary = previous + current
        previous = current
        current = temporary

def fibonacci_less_than(n):
    return take_while_less_than(n, fibonacci())

class FibonacciTestCase(unittest.TestCase):
    def test_fibonacci_less_than_ten(self):
        expected = [1, 2, 3, 5, 8]
        actual = list(fibonacci_less_than(10))
        self.assertEqual(expected, actual)

def evens(xs):
    return itertools.ifilter(is_even, xs)

class EvensTestCase(unittest.TestCase):
    def test_evens(self):
        expected = [0, 2, 4, 6, 8]
        actual = list(evens(range(10)))
        self.assertEqual(expected, actual)

def any(predicate, xs):
    for x in xs:
        if predicate(x):
            return True
    
    return False

def primes():
    composites_to_witnesses = {}

    for n in itertools.count(2):
        if n in composites_to_witnesses:
            for witness in composites_to_witnesses[n]:
                composites_to_witnesses.setdefault(n + witness, []).append(witness)
        else:
            yield n
            composites_to_witnesses[n * n] = [n]

def primes_less_than(n):
    return take_while_less_than(n, primes())

def n_primes(n):
    return itertools.islice(primes(), n)

def factors(n):
    remaining = n

    for prime in primes():
        while divisible_by(remaining, prime):
            yield prime
            remaining = remaining / prime

        if remaining == 1:
            break

def product(xs):
    result = 1
    
    for x in xs:
        result = result * x

    return result

class PrimesTestCase(unittest.TestCase):
    def test_primes(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        actual = list(primes_less_than(20))
        self.assertEqual(expected, actual)

    def test_factors(self):
        expected = [2, 3, 7, 19, 31]
        actual = list(factors(product(expected)))
        self.assertEqual(expected, actual)

def first(xs, predicate = lambda x : True):
    for x in xs:
        if predicate(x):
            return x

def last(xs):
    return list(xs)[-1]

def is_palindromic(n):
    n = str(n)
    return n[:] == n[::-1]

class PalindromicTestCase(unittest.TestCase):
    def test_is_palindromic(self):
        self.assertTrue(is_palindromic(505))
        self.assertTrue(is_palindromic(2002))
        self.assertFalse(is_palindromic(8675309))

def numbers_with_digits(digits, radix = 10):
    start = pow(radix, digits - 1)
    end = pow(radix, digits)
    return range(start, end)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def count_to(n):
    return range(1, n + 1)

def square(n):
    return n * n

def squares(start = 0):
    return itertools.imap(square, itertools.count(start))

def is_perfect_square(n):
    root = math.sqrt(n)
    return root == int(root)

def pythagorean_triplets():
    for square in squares(5):
        for i in range(9, square / 2):
            if is_perfect_square(i):
                j = square - i
                if is_perfect_square(j):
                    yield (int(math.sqrt(i)), int(math.sqrt(j)), int(math.sqrt(square)))

if __name__ == '__main__':
    unittest.main()
