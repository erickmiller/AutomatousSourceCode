#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:

"""
Proposed solution for calculating root mean square of a set of values.
"""

#We need to import the `math` package in order to use the `sqrt` function it
#provides for doing square roots.
import math

def rms(values):
    """
    Returns the _root mean square_ of the given sequence of numerical values.

    :param values:  An iterable of numbers (ints, longs, or floats) for which to
        calculate and return the root mean square.

    :returns float: The root mean square of the given values.
    """

    #Get the squares of the values using a **list comprehension**.
    #
    #This says: for each element in `values`, call that element `v` and
    # multiply it by itself to get the square of the value.
    # Collect these squares as the elements of a new list, in order corresponding
    # to the order of `values`.
    squares = [v*v for v in values]

    #Calculate the sum of the squares.
    #This is easily done using the builtin `sum` function.
    sum_of_squares = sum(squares)

    #Calculate the average ("mean") of the squares.
    #This is simply the sum of the values divided by the number of values.
    #We need to make sure we don't divide by 0!
    if len(squares) == 0:
        raise ValueError('The root mean square is undefined for an empty set.')
    else:
        mean_square = sum_of_squares / float(len(squares))

    #Lastly, take the square root of the mean.
    # Square roots are provided by the `sqrt` function in the `math` package.
    root_mean_square = math.sqrt(mean_square)

    return root_mean_square


if __name__ == '__main__':

    import sys
    
    #Read values from stdin, splitting up the string by whitespace.
    data = sys.stdin.read().split()

    #Convert the values to numbers.
    values = [float(d) for d in data]

    print rms(values)



