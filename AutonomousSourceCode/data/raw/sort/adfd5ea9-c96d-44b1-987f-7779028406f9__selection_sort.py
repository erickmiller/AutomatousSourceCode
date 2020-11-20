def selection_sort(list):
    sorted_list = []
    while len(list) > 0:
        sorted_list.append(list.pop(smallest(list)))
    return sorted_list


def smallest(list):
    smallest = list[0]
    position = 0
    for x in range(len(list)):
        if list[x] < smallest:
            smallest = list[x]
            position = x
    return position


import unittest
class SelectionSortTest(unittest.TestCase):

    unsorted = [3, 8, 15, 1, 6, 3 ,2, 5, 99, 43, 77, 23, 12, 1]
    sorted_list = [1, 1, 2, 3, 3, 5, 6, 8, 12, 15, 23, 43, 77, 99]

    def test_selection_sort(self):
        self.assertEqual(self.sorted_list, selection_sort(self.unsorted))


if __name__ == "__main__":
    unittest.main()
