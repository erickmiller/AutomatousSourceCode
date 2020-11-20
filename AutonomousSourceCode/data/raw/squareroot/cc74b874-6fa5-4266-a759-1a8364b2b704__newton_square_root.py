#########################################################
## Newton's Square Root Approximation
## Bugs to vladimir dot kulyukin at gmail dot com
#########################################################

import math

## global variable that defines error tolerance level
error_tolerance = 0.0001;

def square(x): return x * x

def average(x, y): return (x + y)/2.0

def is_good_enough(guess, n):
    global error_tolerance
    return abs(square(guess) - n) < error_tolerance

def improve_guess(guess, n):
    return average(guess, n/guess)

def sqrt_iter(guess, n):
    if is_good_enough(guess, n):
        return guess
    else:
        print 'improve_guess(', guess, ', ', n, ')=', improve_guess(guess, n)
        return sqrt_iter(improve_guess(guess, n), n)

def newton_sqrt(n):
    ''' Computers Newton's square root approximation of n. '''
    return sqrt_iter(1, n)

## An alternative implementation of Newton's square root approximation
## that uses inner functions and avoids global variables through
## default parameters
def newton_sqrt_inner(n, error_tolerance=0.0001):
    ''' Computes Newton's square root approximation of n. '''
    def is_good_enough_inner(guess):
        return abs(square(guess) - n) < error_tolerance

    def improve_guess_inner(guess, n):
        return average(guess, n/guess)

    def sqrt_iter_inner(guess):
        if is_good_enough_inner(guess):
            return guess
        else:
            print 'improve_guess_inner(', guess, ', ', n, ')=',\
                  improve_guess_inner(guess, n)
            return sqrt_iter_inner(improve_guess_inner(guess, n))

    return sqrt_iter_inner(1)

## Some tests
sqrt_of_2 = newton_sqrt(2)
sqrt_of_3 = newton_sqrt(3)
sqrt_of_4 = newton_sqrt(4)
print 'math.sqrt(2)=', math.sqrt(2), 'newton_sqrt(2)=', sqrt_of_2
print 'math.sqrt(3)=', math.sqrt(3), 'newton_sqrt(3)=', sqrt_of_3
print 'math.sqrt(4)=', math.sqrt(4), 'newton_sqrt(4)=', sqrt_of_4
print "\n";

inner_sqrt_of_2 = newton_sqrt_inner(2)
inner_sqrt_of_3 = newton_sqrt_inner(3)
inner_sqrt_of_4 = newton_sqrt_inner(4)
print 'math.sqrt(2)=', math.sqrt(2), 'newton_sqrt_inner(2)=', inner_sqrt_of_2
print 'math.sqrt(3)=', math.sqrt(3), 'newton_sqrt_inner(3)=', inner_sqrt_of_3
print 'math.sqrt(4)=', math.sqrt(4), 'newton_sqrt_inner(4)=', inner_sqrt_of_4
print "\n";





