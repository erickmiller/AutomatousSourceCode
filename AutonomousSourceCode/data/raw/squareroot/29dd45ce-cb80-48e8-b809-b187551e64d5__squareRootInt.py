"""Calculate the square root of a perfect square"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def squareRootInt(x):
    '''
    Calculate the square root of a perfect square
    :param x: Positive integer
    :return: Square root of the integer (IF AND ONLY IF is a perfect square)
    '''
    # Negative numbers haven't square root
    if x < 0:
        return None

    # 0 <= square root <= x
    value = 0
    while value**2 < x:
        value += 1

    # value**2 >= x
    if value**2 == x:
        return value**2
    else:
        # value**2 > x
        return None