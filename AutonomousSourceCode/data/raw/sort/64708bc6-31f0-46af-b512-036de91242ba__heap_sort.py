#!/usr/bin/env python3


def perc_down(a, start, end):
    largest = 2 * start + 1
    pass

def heapify(a):
    for i in range((len(a) - 2) // 2, 0, -1):
        perc_down(a, i, len(a) - 1)

def heap_sort(a):
    a = a[:]
    heapify(a)
    return a

if __name__ == '__main__':
    assert(heap_sort([]) == [])
    assert(heap_sort([1]) == [1])
    assert(heap_sort([3, 2, 1]) == [1, 2, 3])
    import random
    a = [random.randrange(100) for i in range(100)]
    assert(heap_sort(a) == sorted(a))
