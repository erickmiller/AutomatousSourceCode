def sqrt(x):
    """ Compute square roots using method of Heron of Alexndria.

    Args:
        x: The number of which the square root is to be computed.

    Returns: The square root fo x.

    Raises:
        ValueError: if x is negative
    """
    if x < 0:
        raise ValueError("Cannot compute square root "
                         "of negative number {}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


import sys


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)

if __name__ == '__main__':
    main()