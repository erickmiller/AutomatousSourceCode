# Amy Finnegan
# This file tests the sorting functions in HW3.py

import unittest
import random
import HW3
 
N = 100
random_array = range(1, N)
random.shuffle(random_array)
sorted_array = sorted(random_array)

class TestSortMethods(unittest.TestCase):

  def setUp(self):
    return

  def test_mergeSort(self):
      self.assertEqual(HW3.mergeSort(random_array), sorted_array)
    
  def test_bubblesort(self):
      self.assertEqual(HW3.bubblesort(random_array), sorted_array)
    
  def test_quicksort(self):
      self.assertEqual(sorted(random_array), sorted_array)

if __name__ == '__main__':
    unittest.main()