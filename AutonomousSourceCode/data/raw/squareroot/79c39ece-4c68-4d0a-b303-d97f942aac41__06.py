# Currying

def curry2(f):
    """Returns a function g such that g(x)(y) == f(x, y).

    >>> from operator import add
    >>> add_three = curry2(add)(3)
    >>> add_three(4)
    7
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

# Direct implementations of iterative improvement

def square_root(a):
    """Return the square root of a.

    >>> square_root(9)
    3.0
    """
    x = 1
    while x * x != a:
        x = square_root_update(x, a)
    return x

def square_root_update(x, a):
    return (x + a/x) / 2

def cube_root(a):
    """Return the cube root of a.

    >>> cube_root(27)
    3.0
    """
    x = 1
    while pow(x, 3) != a:
        x = cube_root_update(x, a)
    return x

def cube_root_update(x, a):
    return (2*x + a/(x*x)) / 3

# General iterative improvement

def improve(update, close, guess=1):
    """Iteratively improve guess with update until close(guess) is true."""
    while not close(guess):
        guess = update(guess)
    return guess

def improve(update, close, guess=1, max_updates=100):
    """Iteratively improve guess with update until close(guess) is true or
    max_updates have been applied."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def square_root_improve(a):
    """Return the square root of a.

    >>> square_root_improve(9)
    3.0
    """
    def update(x):
        return square_root_update(x, a)
    def close(x):
        return approx_eq(x * x, a)
    return improve(update, close)

def cube_root_improve(a):
    """Return the cube root of a.

    >>> cube_root_improve(27)
    3.0
    """
    return improve(lambda x: cube_root_update(x, a),
                   lambda x: approx_eq(x*x*x, a))

# Newton's method

def find_zero(f, df):
    """Return a zero of the function f with derivative df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def newton_update(f, df):
    """Return an update function for f with derivative df,
    using Newton's method."""
    def update(x):
        return x - f(x) / df(x)
    return update

def square_root_newton(a):
    """Return the square root of a.

    >>> square_root_newton(9)
    3.0
    """
    def f(x):
        return x*x - a
    def df(x):
        return 2*x
    return find_zero(f, df)

def cube_root_newton(a):
    """Return the cube root of a.

    >>> cube_root_newton(27)
    3.0
    """
    return find_zero(lambda x: x*x*x - a, lambda x: 3*x*x)

def power(x, n):
    """Return x * x * x * ... * x for x repeated n times."""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    """Return the nth root of a.

    >>> nth_root_of_a(2, 64)
    8.0
    >>> nth_root_of_a(3, 64)
    4.0
    >>> nth_root_of_a(6, 64)
    2.0
    """
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)
