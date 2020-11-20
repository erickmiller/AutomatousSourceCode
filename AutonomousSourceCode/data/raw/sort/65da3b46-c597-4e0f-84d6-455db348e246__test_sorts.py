import unittest, random, string
from sorts import merge_sort, insertion_sort

red='\x1b[0;31m'
green='\x1b[0;32m'
teal='\x1b[0;36m'
NC='\x1b[0m' # No Color

class TestSorts(unittest.TestCase):
    '''
    These are some really messy tests to throw a bunch of random strings at us and test if they are sorted via our two algorithms.
    '''

    def setUp(self):
        self.test_data = [self.randomword() for i in range(10)]

    def test_merge_sort(self):

        for test_line in self.test_data:
            merge_sorted = merge_sort(list(test_line))
            tim_sorted = sorted(test_line)
            self.assertEqual(merge_sorted, tim_sorted, '\n\nFailed to be sorted! The input was:\n{}\n\nmerge_sort returned:\n{}\n\nand it should be:\n{}\n'.format(teal + test_line + NC, red + ''.join(merge_sorted) + NC, green + ''.join(tim_sorted) + NC))


    def test_insertion_sort(self):

        for test_line in self.test_data:
            insertion_sorted = insertion_sort(list(test_line))
            tim_sorted = sorted(test_line)
            self.assertEqual(insertion_sorted, tim_sorted, '\n\nFailed to be sorted! The input was:\n{}\n\ninsertion_sort returned:\n{}\n\nand it should be:\n{}\n'.format(teal + test_line + NC, red + ''.join(insertion_sorted) + NC, green + ''.join(tim_sorted) + NC))


    def randomword(self):
        return ''.join(random.choice(string.lowercase) for i in range(50))


if __name__ == '__main__':
    unittest.main()
