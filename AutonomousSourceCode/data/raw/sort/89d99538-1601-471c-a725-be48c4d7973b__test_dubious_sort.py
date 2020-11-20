#! /usr/bin/env python
# test_dubious_sort.py
# 20141015
# David Prager Branner

import os
import sys
sys.path.append(os.path.join('..'))
import dubious_sort as D
import random
import string

def generate_random_list(n):
    while True:
        mess = [random.choice(string.ascii_lowercase) for i in range(n)]
        # We require at least two distinct elements so that sorting is
        # meaningful.
        if len(set(mess)) > 1:
            return mess

def test_n_10():
    lst = generate_random_list(10)
    assert D.sort(lst) == sorted(lst)

#def test_fail():
#    lst = generate_random_list(10)
#    assert lst == sorted(lst)

def test_n_100():
    for i in range(100):
        lst = generate_random_list(100)
        assert D.sort(lst) == sorted(lst)

def test_n_1000():
    for i in range(100):
        lst = generate_random_list(1000)
        assert D.sort(lst) == sorted(lst)

def test_broken_n_1000():
    for i in range(100):
        lst = generate_random_list(1000)
        assert D.sort(lst, broken=True) != sorted(lst)

def test_broken_n_2():
    for i in range(100):
        lst = generate_random_list(2)
        assert D.sort(lst, broken=True) != sorted(lst)
