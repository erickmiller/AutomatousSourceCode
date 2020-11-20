def iSqrt(n):
    """
    Integral square root (by Newton iterations)
    """
    x    = 1
    xOld = 1
    while True:
        aux = ( x + ( n / x ) ) / 2
        if aux == x:
            return x
        if aux == xOld:
            return min(x, xOld)
        xOld = x
        x = aux

def sumSquares(n, m):
    r = n * (n + 1) * (2 * n + 1)
    r /= 6
    r = r % m
    return r

def solve():
    B = 10 ** 15
    k = iSqrt(B)
    m = 10 ** 9
    r = 0
    s = B
    for n in range(1, k+1):
        s2 = B / (n + 1)
        a1 = n * ( sumSquares(s, m) - sumSquares(s2, m) )
        r += a1
        r  = r % m
        a2 = n * n * s
        r += a2
        r  = r % m
        s  = s2
    return r

if __name__ == "__main__":
    result = solve()
    print "Result: %d" % result
