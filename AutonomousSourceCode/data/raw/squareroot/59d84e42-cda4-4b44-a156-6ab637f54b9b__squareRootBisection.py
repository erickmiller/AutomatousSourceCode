"""Calculate the square cube of a float number"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def squareRootBisection(x, precision):
    '''
    Calculate the square root of a float number through bisection method with given precision
    :param x: Float number
    :param precision: Square root precision
    :return: Square root of the float number
    '''
    if x < 0 or precision <= 0:
        return None

    # x>=0
    low = 0.0
    high = x
    value = (low+high)/2
    while abs(value**2-x) > precision:
        if value**2 < x:
            low = value
        else: # value**2 > x
            high = value
        value = (low+high)/2

    return value