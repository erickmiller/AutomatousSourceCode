import pytest
# import sys
# import os
# PACKAGE_PARENT = '..'
# SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from scripts.correlation_parser import sort_tests
from scripts.correlation_parser import sum_tests


# Test sort_tests
# ===============

@pytest.fixture
def def_list():
    mlist = {'a': 1, 'b': 2, 'c': 3, 'd': 0}
    return mlist

def test_sort_tests_weight(def_list):
    sorted_weight = sort_tests(def_list, order='weight')
    assert sorted_weight == [('d', 0), ('a', 1), ('b', 2), ('c', 3)]

def test_sort_tests_weight_reverse(def_list):
    sorted_weight = sort_tests(def_list, order='weight-reverse')
    assert sorted_weight == [('c', 3), ('b', 2), ('a', 1), ('d', 0)]

def test_sort_tests_alphabet(def_list):
    sorted_alphabetical = sort_tests(def_list, order='alphabet')
    assert sorted_alphabetical == [('a', 1), ('b', 2), ('c', 3), ('d', 0)]

def test_sort_tests_alphabet_reverse(def_list):
    sorted_weight = sort_tests(def_list, order='alphabet-reverse')
    assert sorted_weight == [('d', 0), ('c', 3), ('b', 2), ('a', 1)]

def test_sort_tests_error(def_list):
    with pytest.raises(ValueError):
        sorted_weight = sort_tests(def_list, order='non-existing-option')



# Test sum_tests
# ==============

def test_sum_tests():
    """Test sumt test func"""
    data = {'pak1': {'test1': 2, 'test2': 5},
            'pak2': {'test1': 1, 'test3': 7},
            'pak3': {'test1': 1, 'test3': 1},
            'pak4': {'test4': 9, 'test2': 4},
    }

    tests = sum_tests(data)
    assert tests == {'test1': 4, 'test2': 9, 'test3': 8, 'test4': 9}
