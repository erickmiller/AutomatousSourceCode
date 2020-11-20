__author__ = 'mikaeilorfanian'

import random

SIZE_OF_LIST = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 100


def quick_sort(l, sorted_list):
    size = len(l)

    if size == 2:
        if l[0] < l[1]:
            sorted_list.append(l[0])
            sorted_list.append(l[1])
            return
        else:
            sorted_list.append(l[1])
            sorted_list.append(l[0])
            return

    if size < 2:
        if size == 0:
            return
        sorted_list.append(l[0])
        return

    left = []
    right = []
    counter = 0

    while len(left) == 0 or len(right) == 0:

        left = []
        right = []

        pivot = l[counter]
        for i in range(size):
            if l[i] <= pivot:
                left.append(l[i])
            else:
                right.append(l[i])
        counter += 1

    quick_sort(left, sorted_list)
    quick_sort(right, sorted_list)


def initialize_list(arr, size):
    for i in range(size):
        arr.append(random.randrange(LOWER_LIMIT, UPPER_LIMIT))


l = []
sorted_l = []
initialize_list(l, SIZE_OF_LIST)
print l
quick_sort(l, sorted_l)
print sorted_l