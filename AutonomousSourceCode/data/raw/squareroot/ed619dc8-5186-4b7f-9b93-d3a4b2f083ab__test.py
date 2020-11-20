import math
import functools

def deprecate(f):
    f._PRINTED = False
    def func(x):
        if not f._PRINTED:
            print("This function is deprecated. Use something else.")
            f._PRINTED=True
        out = f(x)
        return out
    func = functools.update_wrapper(func, f)
    func.__doc__ = func.__doc__+'\nNote: this function is deprecated'
    return func

@deprecate
def sqrt(x):
    """Return sqare root of input"""
    square = math.sqrt(x)
    return square

