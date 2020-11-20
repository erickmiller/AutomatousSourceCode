import pytest
from random import randint, shuffle

from radix_sort import radix_sort

_RANGE = 100


@pytest.fixture
def make_random():
    return [randint(0, 100) for x in range(_RANGE)]


@pytest.fixture
def make_in_order():
    return [x for x in range(_RANGE)]


@pytest.fixture
def make_in_order_reverse():
    return [x for x in range(_RANGE)][::-1]


def test_radix_sort_random(make_random):
    to_sort = make_random
    assert to_sort != sorted(to_sort)
    assert radix_sort(to_sort) == sorted(to_sort)


def test_radix_sort_in_order(make_in_order):
    to_sort = make_in_order
    assert to_sort == sorted(to_sort)
    assert radix_sort(to_sort) == sorted(to_sort)


def test_radix_sort_reverse(make_in_order_reverse):
    to_sort = make_in_order_reverse
    assert to_sort != sorted(to_sort)
    assert to_sort == sorted(to_sort, reverse=True)
    assert radix_sort(to_sort) == sorted(to_sort)


def test_radix_sort_zero():
    to_sort = []
    assert radix_sort(to_sort) == []


def test_radix_sort_one():
    to_sort = [1]
    assert radix_sort(to_sort) == [1]


def test_radix_sort_small():
    to_sort = [1, 3, 2, 4, 5, 9, 8, 7, 6, 10]
    assert radix_sort(to_sort) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_single_long_int_in_list():
    to_sort = [x for x in range(1000)] + [999999999999999999]
    shuffle(to_sort)
    assert to_sort != sorted(to_sort)
    assert radix_sort(to_sort) == sorted(to_sort)
