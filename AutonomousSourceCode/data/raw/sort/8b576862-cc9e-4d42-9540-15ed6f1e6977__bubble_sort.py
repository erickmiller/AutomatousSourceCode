import unittest


def bubble_sort(array):
    sorted_array = array[::]
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(1, len(sorted_array)):
            if sorted_array[i - 1] > sorted_array[i]:
                sorted_array[i - 1], sorted_array[i] = sorted_array[i], sorted_array[i - 1]
                is_sorted = False

    return sorted_array


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(range(1, 8), bubble_sort([1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(range(1, 8), bubble_sort([5, 1, 6, 3, 4, 2, 7]))
        self.assertEqual(range(1, 8), bubble_sort([7, 6, 5, 4, 3, 2, 1]))


if __name__ == "__main__":
    unittest.main()