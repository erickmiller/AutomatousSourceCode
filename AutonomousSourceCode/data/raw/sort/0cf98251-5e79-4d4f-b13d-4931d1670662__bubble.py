#!/usr/bin/env python
# encoding: utf-8
import unittest


def bubble_sort(array):
    l = len(array)
    for i in xrange(l):
        sorted = False
        location = l
        for j in xrange(1, location - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                sorted = True
                location = j
        if not sorted:
            break
    return array


class BubbleCase(unittest.TestCase):
    def setUp(self):
        pass

    def teatDown(self):
        pass

    def test_bubble(self):
        empty_array = []
        self.assertEqual(bubble_sort(empty_array), [])

        unsorted_array = [5, 1, 3, 6, 7]
        self.assertEqual(bubble_sort(unsorted_array), [1, 3, 5, 6, 7])

        unsorted_negative_array = [-5, 0, 6, -7]
        self.assertEqual(bubble_sort(unsorted_negative_array), [-7, -5, 0, 6])

        sorted_array = [1, 3, 5, 6, 7]
        self.assertEqual(bubble_sort(sorted_array), [1, 3, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()
