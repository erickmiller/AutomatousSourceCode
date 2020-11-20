from random import shuffle


def sort(values):
    while sorted(values) != values:
        shuffle(values)

    return values
