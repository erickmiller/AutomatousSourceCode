from itertools import izip

def sqrt(x):
    """
    Trivial square root implementation.
    """
    return x ** 0.5


def dot(x, y):
    """
    Compute the dot product of two equal length vectors, `x`, and `y`.
    """
    return sum(n * m for n, m in izip(x, y))
