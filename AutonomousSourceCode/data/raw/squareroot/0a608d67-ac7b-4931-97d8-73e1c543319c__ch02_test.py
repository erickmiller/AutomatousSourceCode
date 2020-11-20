'''
7/23/12
Page 24
'''

def testable(x):
    r"""
    The 'testable' funtion returns the square root of its
    parameter, or 3, whichever is larger.
    >>> testable(7)
    3.0
    >>> testable(16)
    4.0
    >>> testable(9)
    3.0
    >>> testable(10) == 10 ** 0.5
    True
    """
    if x < 9:
        return 3.0
    return x**0.5