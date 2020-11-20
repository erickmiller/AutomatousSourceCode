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
    return average(x, a/x)

def average(x, y):
    return  (x + y)/2


       