__author__ = 'cman'

import unittest
from algorithms import merge_sort
from utils import assertions, data


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(MergeSortTest)


class MergeSortTest(unittest.TestCase):

    def test_sort(self):
        test = data.random_ints(100)
        merge_sort.sort(test)
        self.assertTrue(assertions.is_sorted(test))


if __name__ == '__main__':
    unittest.main()
