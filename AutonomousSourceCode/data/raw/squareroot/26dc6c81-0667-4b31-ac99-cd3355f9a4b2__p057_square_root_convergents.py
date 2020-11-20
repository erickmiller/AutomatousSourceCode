#!/usr/bin/python

from project_euler import timeit

cache = {}


def square_root_convergents(upper_limit):
    pell = [0, 1]
    H = [1, 1]

    res = 0
    for n in range(2, upper_limit + 1):
        pell.append(2 * pell[n - 1] + pell[n - 2])
        H.append(H[n - 1] + 2 * pell[n - 1])
        if len(str(H[n])) > len(str(pell[n])):
            res += 1

    return res


timeit(square_root_convergents, 1000)
