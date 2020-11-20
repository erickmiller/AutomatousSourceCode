import pytest
from random import randint

from quick_sort import quick_sort

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


def test_quick_sort_random(make_random):
    to_sort = make_random
    assert to_sort != sorted(to_sort)
    assert quick_sort(to_sort) == sorted(to_sort)


def test_quick_sort_in_order(make_in_order):
    to_sort = make_in_order
    assert to_sort == sorted(to_sort)
    assert quick_sort(to_sort) == sorted(to_sort)


def test_quick_sort_reverse(make_in_order_reverse):
    to_sort = make_in_order_reverse
    assert to_sort != sorted(to_sort)
    assert to_sort == sorted(to_sort, reverse=True)
    assert quick_sort(to_sort) == sorted(to_sort)


def test_quick_sort_zero():
    to_sort = []
    assert quick_sort(to_sort) == []


def test_quick_sort_one():
    to_sort = [1]
    assert quick_sort(to_sort) == [1]


def test_quick_sort_small():
    to_sort = [1, 3, 2, 4, 5, 9, 8, 7, 6, 10]
    assert quick_sort(to_sort) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
