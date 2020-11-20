from random import shuffle, randint


def bogo_sort(array):
    while array != sorted(array):
        shuffle(array)
    return array


if __name__ == '__main__':
    assert bogo_sort([2, 1]) == [1, 2]
    assert bogo_sort([15, 21, 16]) == [15, 16, 21]
    assert bogo_sort([47, 52, 51, 1]) == [1, 47, 51, 52]
    assert bogo_sort([47, 87, 51, 1, 2]) == [1, 2, 47, 51, 87]
    array = [randint(0, 100) for _ in range(10)]
    assert bogo_sort(array) == sorted(array)