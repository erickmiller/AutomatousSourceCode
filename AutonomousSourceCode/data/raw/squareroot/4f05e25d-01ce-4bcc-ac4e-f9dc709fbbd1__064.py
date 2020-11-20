# -*- coding: utf-8 -*-

__title__ = "Odd period square roots"

def solve():
    
    from math import sqrt
    n = 23

    def get_period(n):
        root = int(sqrt(n))
        m, d, a = 0, 1, root
        seq = [(0, 1, root)]
        while True:
            m = d*a - m
            d = (n - m*m)/d
            if d == 0:
                return 0
            a = int((root+m)/d)
            if seq.count((m, d, a)) > 0:
                return len(seq) - seq.index((m, d, a))
            else:
                seq.append((m, d, a))

    s = 0
    for n in xrange(2, 10001):
        d = get_period(n)

        if d % 2 != 0:
            s = s + 1

    return s



