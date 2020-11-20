#!/usr/bin/env python2.6
"""
The Babylonian method of estimating a square root.
"""


def sqrt(x, eps=1e-6):
    r = x * 1.
    while abs(x - r * r) > eps:
        r = 0.5 * (r + x / r)
    return r


print sqrt(256)
