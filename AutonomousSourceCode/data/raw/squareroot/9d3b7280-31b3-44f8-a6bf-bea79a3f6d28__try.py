# How to find the square root of 2?

f = lambda x: x*x - 2
df = lambda x: 2*x
# find_zero(f, df)

# How to find the cube root of 729?

g = lambda x: x*x*x - 729
dg = lambda x: 3*x*x
# find_zero(g, dg)

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def square_root(a):
    def f(x):
        return x*x - a
    def df(x):
        return 2*x
    return find_zero(f, df)

def cube_root(a):
    return find_zero(lambda x: x*x - a,
                     lambda x: 2*x)

def power(x, n):
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def root(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)



def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance

def square_root(a):
    """Return the square root of a.

    >>> square_root(9)
    3.0
    """
    x = 1
    def update(x):
        return square_root_update(x ,a)
    def close(x):
        return approx_eq(x*x, a)
    return improve(update, close)

def square_root_update(x, a):
    return (x + a/x) / 2

def cube_root(a):
    return improve(lambda x: cube_root_update(x, a),
                   lambda x: approx_eq(pow(x, 3), a))

def cube_root_update(x, a):
    return (2*x + a/(x*x)) / 3
