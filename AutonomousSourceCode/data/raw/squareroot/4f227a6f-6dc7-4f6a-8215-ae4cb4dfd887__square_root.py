#!/usr/bin/python
import math

def square_root(a):
    x = a / 2.0
    epsilon = 0.00000001
    while True:
        y = (x + a/x) / 2.0
        if abs(x-y) <= epsilon:
            break
        x = y
    return x

