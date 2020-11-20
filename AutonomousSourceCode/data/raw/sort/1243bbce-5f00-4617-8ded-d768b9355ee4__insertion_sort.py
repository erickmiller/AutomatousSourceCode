import unittest

def insertion_sort(array):
    for i in range(1, len(array)):
        current = i
        while array[current] < array[current - 1] and current > 0:
            array[current], array[current - 1] = array[current - 1], array[current]
            current -= 1
    return array

class TestInsertionSort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(insertion_sort([]), [])

    def test_integers(self):
        self.assertEqual(insertion_sort([4, 7, 1, 8, 4, 2, 7, 2, 1, 0]), sorted([4, 7, 1, 8, 4, 2, 7, 2, 1, 0]))

    def test_strings(self):
        self.assertEqual(insertion_sort(['zebra', 'penguin', 'aardvark', 'basilisk']), sorted(['zebra', 'penguin', 'aardvark', 'basilisk']))

if __name__ == '__main__':
    unittest.main()
