#!/usr/bin/python
import math

def print_n(s,n):
    for i in range(n):
        print s

print_n('pants',5)

epsilon = 0.0000001

new_root = 0.0

def square_root(a):
    new_root = a/3.0
    old_root = 0.0
    while abs(old_root-new_root) > epsilon:
        old_root = new_root
        new_root = (new_root+a/new_root)/2.0

    return new_root

square_root(100)

def test_square_root(a):
    newton = square_root(a)
    official = math.sqrt(a)
    print '%s\t%s\t%s\t%s' % (a,newton,official,abs(newton-official))

test_square_root(345)   
