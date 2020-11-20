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

def getSum(n):
    x = iSqrt(n)
    if x * x == n:
        return 0
    x = n * 10 ** 200
    y = iSqrt(x)
    y /= 10
    r = 0
    while y > 0:
        r += y % 10
        y /= 10
    return r

def solve():
    r = 0
    for k in range(1, 101):
        r += getSum(k)
    return r

if __name__ == "__main__":
    result = solve()
    print "Result: %d" % result
