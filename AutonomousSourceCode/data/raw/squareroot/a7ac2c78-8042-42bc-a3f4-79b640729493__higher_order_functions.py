def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-14):
    return abs(x - y) < tolerance
    
def average(x, y):
    return (x + y)/2
    
def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)
    
def newton_update(f, df):
    return lambda x: x - f(x) / df(x)

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)
    
def power(x, n):
    """Return x * x * x * ... * x for x repeated n times."""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product
    
def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n - 1)
    return find_zero(f, df)
    
def curried_power(x):
    return lambda y: power(x, y)
    
def curried_nth_power(x):
    return lambda y: power(y, x)
    
def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1
        
def curry2(f):
    """Return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
    
def uncurry2(g):
    """Return a two-argument version of the given curried function."""
    def f(x, y):
        return g(x)(y)
    return f
    
def trace(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped
    
def tracetest(fn):
    return 5
    
@tracetest
def ftest():
    return 26
    
@trace
def quadruple(x):
    return 4 * x
    