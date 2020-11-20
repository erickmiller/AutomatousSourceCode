import random


def insertion_sort(ls):
    for i in xrange(1, len(ls)):
        key = ls[i]
        j = i - 1
        while j >= 0 and ls[j] > key:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key


def is_sorted(ls):
    return ls == sorted(ls)


def random_ls(len, frm, to):
    return [random.randint(frm, to) for _ in xrange(len)]


def test_insertion_sort_simple():
    ls = [5, 2, 4, 6, 1, 3]
    insertion_sort(ls)
    assert ls == [1, 2, 3, 4, 5, 6]


def test_insertion_sort_random():
    for i in [10, 100, 1000]:
        ls = random_ls(i, 0, i//2)
        insertion_sort(ls)
        assert is_sorted(ls)


def test_insertion_sort_trivial():
    for i in [10, 100, 1000]:
        ls = range(i)
        insertion_sort(ls)
        assert is_sorted(ls)
