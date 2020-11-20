from chapter6Exercises import *

def squareRoot(a):
    if a > 1:
        x = a - 1.0
    else:
        x = 1.0
    y = (x + (a / x)) / 2
    epsilon = 0.00000001
    while abs(y-x) >= epsilon:
        x = y
        y = (x + (a / x)) / 2
    return y


def squareRootTest(n):
    a = 1.0
    while a < n:
        b = squareRoot(a)
        c = math.sqrt(a)
        d = abs(b - c)
        print a, " ", b, " " * (15 - len(str(b))), c, " " * (15 - len(str(c))),
        print d
        a = a + 1


def evalLoop():
    end = "done"
    n = raw_input()
    while n != end:
        print eval(n)
        n = raw_input()
    return eval(n)

def estimate_pi():
    k = 0.0
    last_term = 1.0
    sigma = 0
    while last_term > 1e-15:
        last_term = ((math.factorial(4.0 * k)) * (1103.0 + 26390.0 * (k))) \
        / ((math.factorial(k)**4.0) * (396.0**(4.0 * k)))
        k += 1.0
        sigma += last_term
    result = ((2 * math.sqrt(2)) / 9801) * sigma
    print 1 / result


