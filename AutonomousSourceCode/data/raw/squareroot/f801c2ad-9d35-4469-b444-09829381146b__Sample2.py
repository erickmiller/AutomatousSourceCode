__author__ = 'gokhan'

import math

# class declaration

class myFirstClass():
    print "myFirstClass"


    # contractor declaration
    def __init__(self, name):
        self.name = name
        print name

    # function declaration
    def myFirstFunction(self):
        print "myFirstFunction"

    # apply function

    def func(x, y, z): return x + y + z

    print apply(func, (2, 3, 4))
    f = lambda x, y, z: x + y + z
    print apply(f, (2, 3, 4))


    # programmer-defined exception


class NegativeNumberError(ArithmeticError):
    pass


def squareRoot(number):
    if number < 0:
        raise NegativeNumberError, "Square root of negative number not permitted"
    return math.sqrt(number)


while 1:
    try:
        userValue = float(raw_input("\nPlease enter a number: "))
        print squareRoot(userValue)
    # float raises ValueError if input is not numerical
    except ValueError:
        print "The entered value is not a number"
    # squareRoot raises NegativeNumberError if number is negative
    except NegativeNumberError, exception:
        print exception
    else:
        break
