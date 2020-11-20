'''
Calculating the digital sum of the decimal digits of irrational square roots.
'''

import decimal
import intlib
decimal.getcontext().prec = 105  # 有効桁数を105桁に.


def square_root(n):
    ans = []
    p = 0
    c = n
    for i in range(100):
        x = 0
        while x * (20 * p + x) <= c:
            x += 1
        x = x - 1
        ans.append(x)
        c = (c - x * (20 * p + x)) * 100
        p = 10 * p + x

    return ans


def cheat():
    'decimalモジュールの有効桁数を操作するチート?'
    ans = 0
    dec = decimal.Decimal
    for n in range(1, 100):
        if not intlib.is_square(n):
            ans += sum(int(d) for d in str(dec(n) ** dec(.5))[:101]
                       if d != '.')
    return ans


def main():
    return sum(sum(square_root(n)) for n in range(1, 100)
               if n not in (n * n for n in range(1, 10)))

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
    t1 = time.time()
    print(cheat())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
