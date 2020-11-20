import sys
import os
import math

def my_range(n):
    i = 1.0
    while i <= n:
	yield i
	i = i + 1.0

def square_root(a, x):
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x

def test_square_root(x):
    for i in my_range(x):
	a = square_root(i, i+1)
	b = math.sqrt(i)
	print i, '\t',
        print a, '\t',
	print b, '\t',
	print abs(b - a)

if __name__ == '__main__':
    prompt = "Enter the limit : "
    value = float(raw_input(prompt))
    test_square_root(value)

