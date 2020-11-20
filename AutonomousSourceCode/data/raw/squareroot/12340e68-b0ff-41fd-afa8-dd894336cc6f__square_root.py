def find_root(a, b):
    i = float(a)
    step = float(b)
    return step - ((step ** 2 - i) / (2 * step))


def square_root(in_put, precision):
    """
    :param input: Takes an input number
    :param precision: Takes a precision to output
    :return: The square root of the input number
    """
    in_put = float(in_put)
    precision = 1 / (10 ** float(precision))

    if in_put < 0:
        raise Exception("The square root of a negative number is non-real")
    elif in_put == 0:
        return 0
    else:
        error = None
        step = int(in_put) - 1
        while error > precision or error is None:
            step = find_root(in_put, step)
            error = step ** 2 - in_put
        return step


if __name__ == "__main__":
    print square_root(4, 4)
    print square_root(10.9, 100)
