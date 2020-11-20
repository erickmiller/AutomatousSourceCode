from sort import quicksort, mergesort, straight_mergesort, bubblesort
import random
import pytest


@pytest.fixture
def seq():
    return random.sample(range(10 ** 2), 10)


def test_quicksort(seq):
    assert_unsorted(seq)
    assert_sorted(quicksort(seq))


def test_mergesort(seq):
    assert_unsorted(seq)
    assert_sorted(mergesort(seq))


def test_straight_mergesort(seq):
    assert_unsorted(seq)
    assert_sorted(straight_mergesort(seq))


def test_bubblesort(seq):
    assert_unsorted(seq)
    assert_sorted(bubblesort(seq))


def sortable(func):
    def _wrapper(seq):
        if len(seq) < 2:
            return
        return func(seq)
    return _wrapper


@sortable
def assert_sorted(seq):
    for i in range(len(seq) - 1):
        assert seq[i] <= seq[i + 1]


@sortable
def assert_unsorted(seq):
    assert any(seq[i] > seq[i + 1] for i in range(len(seq) - 1))
