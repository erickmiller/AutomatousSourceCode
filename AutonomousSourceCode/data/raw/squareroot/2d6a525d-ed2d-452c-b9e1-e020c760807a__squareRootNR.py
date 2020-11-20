"""Calculate the square cube of a float number"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def squareRootNR(x, precision):
    '''
    Calculate the square root of a float number through Newton-Raphson method with given precision
    :param x: Float number
    :param precision: Square root precision
    :return: Square root of the float number
    '''
    if x < 0 or precision <= 0:
        return None

    # x>=0
    value = x/2.0
    while abs(value**2 - x) > precision:
        value = value - (value**2 - x)/(2*value)
    return value