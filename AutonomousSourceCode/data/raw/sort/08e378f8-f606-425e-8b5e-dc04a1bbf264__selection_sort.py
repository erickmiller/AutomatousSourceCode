import unittest


def selection_sort(array):
    sorted_array, length = array[::], len(array)

    for i in range(length):
        min_idx = i
        for j in range(min_idx, length):
            if sorted_array[j] < sorted_array[min_idx]:
                min_idx = j
        sorted_array[i], sorted_array[min_idx] = sorted_array[min_idx], sorted_array[i]

    return sorted_array


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(range(1, 8), selection_sort([1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(range(1, 8), selection_sort([5, 1, 6, 3, 4, 2, 7]))
        self.assertEqual(range(1, 8), selection_sort([7, 6, 5, 4, 3, 2, 1]))
        self.assertEqual([], selection_sort([]))
        self.assertEqual([10], selection_sort([10]))

if __name__ == "__main__":
    unittest.main()