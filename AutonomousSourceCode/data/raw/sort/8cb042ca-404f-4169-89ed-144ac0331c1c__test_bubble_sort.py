import unittest
import bubble_sort

class BubbleSortTest(unittest.TestCase):

    def is_list_sorted(lst):
        return all([lst[i] <= lst[i+1] for i in xrange(len(lst)-1)])

    def test_bubble_sort():
        lists = (
            [0,5,2,-1],
            []
            [-10,-3,0.1,3])

        
