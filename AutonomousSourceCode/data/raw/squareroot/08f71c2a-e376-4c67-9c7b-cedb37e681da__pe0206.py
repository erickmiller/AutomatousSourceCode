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

pattern = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def check(x):
    n = x * x
    for x in pattern:
        if n % 10 != x:
            return False
        n /= 100
    return True

def solve():
    start = iSqrt(19293949596979899)
    start /= 10
    n = start
    while n > 0:
        if check(10 * n + 3):
            return 100 * n + 30
        if check(10 * n + 7):
            return 100 * n + 70
        n -= 1
    return 0

if __name__ == "__main__":
    result = solve()
    print "Result: %d" % result
