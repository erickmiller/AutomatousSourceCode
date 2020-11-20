def sqrt(x):
    '''
    Compute square roots using the method of Heron of Alexandria.
    :param x: The number for which the square root is to be computed.
    :return: The square root of x.
    '''

    if x < 0:
        raise ValueError("Cannot compute square root "
                         "of negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ValueError:
        print("Cannot compute square root of negative number")
    finally:
        print("Finally called")

    print("Program execution continues normally here")


if __name__ == '__main__':
    main()
