#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Project Euler Solution 057

Copyright (c) 2011 by Robert Vella - robert.r.h.vella@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import cProfile

_roots = [
    (1, 1)
]

_square_numbers = {1}

def _nearest_whole_square_root(n):
    while _roots[-1][0] < n:
        next_root = _roots[-1][1] + 1
        square_number = next_root*next_root

        _square_numbers.add(square_number)

        _roots.append((square_number, next_root))

    for i in xrange(1, len(_roots)):
        if _roots[i][0] > n:
            return _roots[i - 1][1]

def _is_square_number(n):
    return n in _square_numbers

class _SquareRootFraction(object):
    """
        (sqrt(a) + b)/c
    """
    def __init__(self, a, b, c, nearest_whole_number):
        self.a = a
        self.nearest_whole_number = nearest_whole_number

        self.b = b
        self.c = c

    def reciprocal(self):
        new_c = (self.b*self.b - self.a) / -self.c
        new_b = -self.b

        whole_number = (self.nearest_whole_number + new_b) / new_c

        new_b -= whole_number * new_c

        return _SquareRootFraction(self.a, new_b, new_c, self.nearest_whole_number)

def get_period(n):
    if _is_square_number(n):
        return 0

    nearest_whole_number = _nearest_whole_square_root(n)

    current_reciprocal = _SquareRootFraction(n, -nearest_whole_number, 1, nearest_whole_number).reciprocal()
    period = 1

    while not (current_reciprocal.b == -nearest_whole_number and current_reciprocal.c == 1):
        current_reciprocal = current_reciprocal.reciprocal()
        period += 1

    return period

def get_number_of_odd_periods_up_to(n):
    return sum(1 for i in xrange(1, n + 1) if get_period(i) % 2 == 1)

def get_answer():
    return get_number_of_odd_periods_up_to(10000)

    
if __name__ == "__main__":
    cProfile.run("print(get_answer())")
