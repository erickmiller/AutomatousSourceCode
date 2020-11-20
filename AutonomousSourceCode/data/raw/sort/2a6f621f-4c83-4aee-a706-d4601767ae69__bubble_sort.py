# placeholder for bubble sort
import unittest


class Bubbler(object):
    def __init__(self, sample):
        ''' sample is the list to sort
        '''
        self.sample = sample

    @property
    def sorter(self):
        ''' implement bubble sort here
        '''
        pass

    def __repr__(self):
        return 'Bubbler({})'.format(self.sample)


class BubblerTestCases(unittest.TestCase):

    def test_simple(self):
        x1 = [1, 2, 3, 4, 5]
        b = Bubbler(x1)
        self.assertEquals(b.sorter, sorted(b.sample))

    def test_negatives(self):
        x2 = [4, 5, 23, 5, 6, 1, 6, -1, 0.3]
        b = Bubbler(x2)
        self.assertEquals(b.sorter, sorted(b.sample))

    def test_all_negatives(self):
        x3 = [-1, -4, -3, -2, -5]
        b = Bubbler(x3)
        self.assertEquals(b.sorter, sorted(b.sample))

    def test_decimals(self):
        x4 = [0.3, 0.2, 0.1, 0.4, -0.5, -0.3]
        b = Bubbler(x4)
        self.assertEquals(b.sorter, sorted(b.sample))


if __name__ == '__main__':
    unittest.main()
