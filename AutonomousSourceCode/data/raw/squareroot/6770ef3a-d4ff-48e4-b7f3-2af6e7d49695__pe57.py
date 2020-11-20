#! /usr/bin/env python3

def pe57(limit=1000):
    """
    Investigate the expansion of the continued fraction
    for the square root of two.
    """
    n, d = 3, 2
    cnt = 0
    for a in range(limit + 1):
        # n, d = n + (d << 1), n + d
        nn = n
        n += d << 1
        d += nn
        if len(str(n)) > len(str(d)):
            cnt += 1
    return cnt

def calc(n):
    nd13 = n // 13
    return (nd13 << 1) + ((n - nd13 * 13) >> 3)

def pe57a(n=1000):
    return calc(n)

if __name__ == "__main__":
    # print(pe57())
    print(pe57a())
