import pytest
from random import randint

from merge_sort import merge_sort

_RANGE = 1000


@pytest.fixture
def make_random():
    return [randint(0, 100) for x in range(_RANGE)]


@pytest.fixture
def make_in_order():
    return [x for x in range(_RANGE)][::-1]


@pytest.fixture
def make_in_order_reverse():
    return [x for x in range(_RANGE)]


def test_insertion_sort_random(make_random):
    to_sort = make_random
    assert to_sort != sorted(to_sort, reverse=True)[::-1]
    assert merge_sort(to_sort) == sorted(to_sort, reverse=True)


def test_insertion_sort_in_order(make_in_order):
    to_sort = make_in_order
    assert to_sort == sorted(to_sort, reverse=True)
    assert merge_sort(to_sort) == sorted(to_sort, reverse=True)


def test_insertion_sort_reverse(make_in_order_reverse):
    to_sort = make_in_order_reverse
    assert to_sort != sorted(to_sort, reverse=True)
    assert to_sort == sorted(to_sort)
    assert merge_sort(to_sort) == sorted(to_sort, reverse=True)
