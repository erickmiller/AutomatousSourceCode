
def sqrt(x):
    """
    give square root
    """
    if x >= 0:
        """
        if x is positive"""
        return x ** 0.5
    return (x + 0j) ** 0.5

def add(a, b):
    temp = a + b
    return temp

def f(x, y):
    return x ** 2 + x * y + y ** 2

res = f(2, 3) + sqrt(4)
print res


