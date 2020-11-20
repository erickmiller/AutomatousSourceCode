def gcd(a, b):
    if a == b:
        return a
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a%b)

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

def solve():
    B = 10 ** 12
    s = set()
    for a in range(2, 10**4):
        a3 = a ** 3
        for b in range(1, a):
            b2 = b ** 2
            if b2 * (a3 + 1) >= B:
                break
            c = 1
            n = a3 * b * c * c + c * b2
            while n <= B:
                r = iSqrt(n)
                if r * r == n:
                    s.add(n)
                c += 1
                n = a3 * b * c * c + c * b2
    return sum(s)

if __name__ == "__main__":
    result = solve()
    print "Result: %d" % result
