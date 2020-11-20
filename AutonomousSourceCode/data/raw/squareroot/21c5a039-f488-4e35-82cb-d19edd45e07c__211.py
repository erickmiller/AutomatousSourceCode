#/bin/python

# http://projecteuler.net/problem=211

'''
For a positive integer n, let 2(n) be the sum of the squares of its divisors. For example,

2(10) = 1 + 4 + 25 + 100 = 130.
Find the sum of all n, 0  n  64,000,000 such that 2(n) is a perfect square.
'''

from prime import get_divisors

def is_perfect_square(n):
    root = n**0.5
    return root == int(root)

tot = sum((n for n in range(0,60000000) if is_perfect_square(sum(get_divisors(n)))))
#tot = sum((n for n in range(0,600000) if is_perfect_square(sum(get_divisors(n)))))
print(tot)
