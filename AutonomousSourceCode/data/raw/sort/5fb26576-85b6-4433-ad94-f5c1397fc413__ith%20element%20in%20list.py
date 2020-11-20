#
##############################################
# Faizan Syed (20571514)
# CS 116 Winter 2015
# Assignment 7 Problem 4 (get sorted number)
##############################################
#

import check

# ith_in_sorted(lst, i) produces the ith element in lst if you were to sort lst from
#  smallest to largest
# ith_in_sorted: (listof Int) Int -> Int
# Examples:
# ith_in_sorted([17, -5, 3, 0, 2, 100], 2) => 2
# ith_in_sorted([300, 200, 100], 0) => 100

def ith_in_sorted(lst, i):
    separator = lst[0]
    smaller = list(filter(lambda x: i > x, lst))
    larger = list(filter(lambda y: i < y, lst))
    if len(smaller) == i:
        return lst[i]
    elif len(smaller) > i:
        return ith_in_sorted(smaller, i)
    else:
        return ith_in_sorted(larger, (i - len(smaller) - 1))

check.expect("T1", ith_in_sorted([300, 200, 100], 0), 100)
check.expect("T2", ith_in_sorted([17, -5, 3, 0, 2, 100], 2), 2)