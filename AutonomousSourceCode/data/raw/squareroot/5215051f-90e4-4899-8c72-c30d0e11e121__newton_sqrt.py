# encoding: utf-8
'''
Square root using Newton's method
recusive method example
'''

import math

PRECISION = 0.001
INITIAL_GUESS = 1.0

def __sqrt_iter(guess, x):
    if __good_enough(guess, x):        
        print guess        
    else:
        __sqrt_iter(__improve(guess, x), x)
        
def __improve(guess, x):
    return __average(guess, (x / guess))

def __average(x, y):
    return (x + y) / 2
    
def __good_enough(guess, x):
    return math.fabs((guess**2 - x)) < PRECISION
    
def nw_sqrt(x, initial_guess=INITIAL_GUESS):
    '''
    Return the square root of a number using the Newton's method based on proximity.
    
    #### needs some fixes ###
    >>> nw_sqrt(36, 1.0)
    6.00000000533    
    '''
    __sqrt_iter(initial_guess, x)   


if __name__ == '__main__':
    import doctest
    doctest.testmod()