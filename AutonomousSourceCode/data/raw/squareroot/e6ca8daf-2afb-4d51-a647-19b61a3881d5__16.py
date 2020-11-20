import math
import sys

def summation(n, term):
    return sum(term(k) for k in range(1, n + 1))

def invSquareSum(n):
    return summation(n, lambda k : 1 / (k * k))

# NOTE: if you try using 1e3 here, you'll get an error.  Why is that,
# and how could you fix it inside summation()?
x = invSquareSum(1000)
print(math.sqrt(6 * x))

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def goldenUpdate(x):
    return 1 / x + 1

def squareCloseToSuccessor(x):
    return approxEq(x * x, x + 1)

def approxEq(x, y, epsilon=1e-15):
    return abs(x - y) < epsilon

print(improve(goldenUpdate, squareCloseToSuccessor))

def interpolate(x, y, f=0.5):
    return (1 - f) * x + f * y

def cubeRoot(a, f=0.5):
    iters = 0
    def cubeRootUpdate(x):
        nonlocal iters
        iters += 1
        return interpolate(x, a / (x * x), f)
    def cubeRootClose(x):
        return approxEq(x * x * x, a)
    ret = improve(cubeRootUpdate, cubeRootClose)
    print('iters: {0}'.format(iters))
    return ret

# NOTE: convergence speed depends on the initial guess and iteration
# algorithm.  How can you compute the optimal value of f?  Can you
# generalize this process for any improve() call?
print(cubeRoot(8))
print(cubeRoot(8, 1/4))
print(cubeRoot(8, 1/3))

from operator import add

def curry2(f):
    """
    >>> curry2(add)(41)(1)
    42
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def myAdd(a, b):
    return a + b

def curry(f):
    """
    >>> curry(myAdd)(41)(1)
    42
    >>> curry(myAdd)(a=41)(b=1)
    42
    >>> curry(myAdd)(41)(b=1)
    42
    >>> curry(myAdd)(a=41)(1)
    Traceback (most recent call last):
        ...
    TypeError: myAdd() got multiple values for argument 'a'

    NOTE: what other tests should be added?
    """
    def g(*args, **kwargs):
        def h(*moreArgs, **moreKwargs):
            nonlocal args
            nonlocal kwargs
            args += moreArgs
            kwargs.update(moreKwargs)
            return f(*args, **kwargs)
        return h
    return g

if __name__ == '__main__':
    from doctest import testmod
    print(testmod())
