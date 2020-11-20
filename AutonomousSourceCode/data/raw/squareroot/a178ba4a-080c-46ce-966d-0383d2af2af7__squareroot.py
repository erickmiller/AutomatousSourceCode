import math

def sqrt(x):
    """Approximates the square root of the number x. 

    This function is provided for demonstration purposes, 
    you should use the provided math.sqrt(x) instead.
    
    """
    return sqrt_helper(1.0, x)     # We chose 1.0 as our arbitrary starting value.


def sqrt_helper(guess, x):
    """Helper function that actually performs the algorithm for sqrt(x)"""
    if good_enough(guess, x):    # We'll call it good if the square 
        return guess                            # of our guess is within 0.0001 of our number x
    return sqrt_helper(improve_guess(guess, x), x)

def good_enough(guess, x):
    """Return true if close enough, otherwise false."""
    if math.fabs(guess**2 - x) < 0.001:     # Good enough if absolute value of difference less than arbitrary amount 0.001
        return True
    return False

def improve_guess(guess, x):
    """Improves the guess by Heron's method

    That is, average the guess and the quotient of x and the guess.

    """
    return (guess + (x / guess)) / 2.0

def example_sqrt(x):
    """Prints example output in a string"""
    print("The square root of " + str(x) + " is " + str(sqrt(x)))
    return None

i = 1
while(i < 10):
    example_sqrt(i)
    i += 1
