#!/usr/bin/env python
import math


def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False


def count_neighbourhoods(r):
    cnt = 0
    for i in range(int(math.ceil(math.sqrt(r)))):
        if is_square(r - i * i):
            cnt += 4
    return cnt


if __name__ == '__main__':
    t = input()
    for i in range(t):
        a = map(int, raw_input().strip().split(" "))
        if a[1] >= count_neighbourhoods(a[0]):
            print "possible"
        else:
            print "impossible"
