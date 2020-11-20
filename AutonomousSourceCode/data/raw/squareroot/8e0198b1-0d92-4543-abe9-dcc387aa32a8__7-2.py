#!/usr/bin/env python


def square_root(a):
    eps = 1e-8
    x = 1.0
    y = 2.0
    cnt = 1
    while abs(y - x) > eps:
        x = y
        y = (x + a / x) / 2
        print 'iter', cnt, '\ty=', y
        cnt = cnt + 1
    return y

print square_root(10)

