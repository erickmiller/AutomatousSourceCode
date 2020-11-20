# coding=utf-8


def my_square_root(n, precision=None):
    if precision is None:
        precision = 5

    start = 0.01
    end = max(float(n), 1.0)
    max_e = 10.0 ** (-precision)
    while True:
        mid = start + (end - start) / 2.0
        e = n - (mid * mid)
        if abs(e) <= max_e:
            return mid
        elif e < 0:
            end = mid
        else:
            start = mid
