
def CountingSort(values, min_key, max_key, key=lambda x: x):
  counts = [0 for _ in xrange(max_key - min_key + 1)]
  for value in values:
    index = key(value) - min_key
    counts[index] += 1

  for i in xrange(1, len(counts)):
    counts[i] += counts[i - 1]

  sorted_values = [None for _ in values]
  for value in reversed(values):
    key_value = key(value)
    index = counts[key_value - min_key] - 1
    sorted_values[index] = value
    counts[key_value - min_key] -= 1
  return sorted_values


def InPlaceCountingSort(values, min_key, max_key, key=lambda x: x):
  """Not stable sort!"""
  counts = [0 for _ in xrange(max_key - min_key + 1)]
  for value in values:
    index = key(value) - min_key
    counts[index] += 1

  j = len(values)
  for i in xrange(len(counts) - 1, -1, -1):
    i_key = i + min_key
    k = j - 1
    for _ in xrange(counts[i]):
      while key(values[k]) != i_key:
        k -= 1
      Swap(values, j - 1, k)
      j -= 1
      k -= 1


def Swap(values, i, j):
  temp = values[i]
  values[i] = values[j]
  values[j] = temp


def GetDigitFunction(digit):
  mask = 10 ** digit

  def GetDigit(x):
    x /= mask
    x -= x / 10 * 10
    return x

  return GetDigit


def NumDecimals(value):
  count = 0
  while True:
    count += 1
    value /= 10
    if not value:
      return count


def RadixSort(values):
  for digit in xrange(NumDecimals(max(values))):
    values = CountingSort(values, 0, 9, key=GetDigitFunction(digit))
  return values


import unittest
import random
import copy


class TestCountingSort(unittest.TestCase):

  def setUp(self):
    self.longMessage = True

  def test_counting(self):
    values = [random.randint(1,10) for _ in xrange(100)]
    sorted_values = CountingSort(values, 1, 10)
    self.assertEqual(sorted(values), sorted_values,
                     msg='original={} sorted={}'.format(values, sorted_values))

  def test_InPlaceCountingSort(self):
    values = [random.randint(1,5) for _ in xrange(20)]
    original_values = copy.deepcopy(values)
    InPlaceCountingSort(values, 1, 10)
    self.assertEqual(sorted(original_values), values,
                     msg='original={} sorted={}'.format(original_values,
                                                        values))


class TestRadixSort(unittest.TestCase):

  def setUp(self):
    self.longMessage = True

  def test_digit(self):
    for x in xrange(0, 10):
      self.assertEqual(x, GetDigitFunction(0)(x))
    for x in xrange(10, 20):
      self.assertEqual(1, GetDigitFunction(1)(x))
    for x in xrange(20, 30):
      self.assertEqual(2, GetDigitFunction(1)(x))

    self.assertEqual(0, GetDigitFunction(1)(4))

  def test_NumDecimals(self):
    self.assertEqual(1, NumDecimals(0))
    self.assertEqual(1, NumDecimals(1))
    self.assertEqual(2, NumDecimals(10))
    self.assertEqual(2, NumDecimals(11))
    self.assertEqual(3, NumDecimals(100))

  def test_RadixSortDense(self):
    values = [random.randint(1,10000) for _ in xrange(10)]
    sorted_values = RadixSort(values)
    self.assertEqual(sorted(values), sorted_values,
                     msg='original={} sorted={}'.format(values, sorted_values))

  def test_RadixSortSparse(self):
    values = [random.randint(1,10) for _ in xrange(100)]
    sorted_values = RadixSort(values)
    self.assertEqual(sorted(values), sorted_values,
                     msg='original={} sorted={}'.format(values, sorted_values))
