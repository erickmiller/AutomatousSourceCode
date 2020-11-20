#Basic calculator project
import math
def cube(n):
    """
    Returns the cube of the number n
    """
    return n**3

def squareroot(n):
    """
    Returns the square root of the number n. If n < 0, 
    then return the string "NAN" (not a number)
    """
    return math.sqrt(n)

def negate(n):
    """ Return negative n
    """
    return -n

def factorial(n):
    """Return n factorial
    The factorial of anything <= 1 is 1
    >>> factorial(4)
    24
    """
    return math.factorial(n)

