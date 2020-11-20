def sqrt(x):
    '''Compute square roots using the method of Helon of Alexandria.

        Args: 
            X: The number for which the square root is be computed

        Returns:
            The square root of x.

        Raises:
            ValueError: If x is Negative
    '''
    if x < 0:
        raise ValueError("Cannot compute square root of negative number {}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x/ guess) / 2.0
        i += 1
    return guess

import sys

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never printed")
        print(sqrt(6)) 
    except ValueError as e:
        print(e, file=sys.stderr)

    print("Program execution continutes normally here")

if __name__ == '__main__':
    main()