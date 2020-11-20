__author__ = 'nunoe'


def newton_raphson_root(value, power, epsilon):
    """ function used to find the root of a given value through the Newton-Raphson method

    :param value: int, number for which we want to find the root
    :param power: int, power that turns the root into the given value
    :param epsilon: float, tolerance used when testing the root
    :return: float, the root of the given value
    """
    result = value / 2.0

    while abs(result ** power - value) >= epsilon:
        result += (value - result ** power) / (power * result ** (power - 1))
    return result

if __name__ == '__main__':
    print 'The cubic root of 27 is ' + str(newton_raphson_root(27, 3, 0.001))
    print 'The square root of 9 is ' + str(newton_raphson_root(9, 2, 0.001))