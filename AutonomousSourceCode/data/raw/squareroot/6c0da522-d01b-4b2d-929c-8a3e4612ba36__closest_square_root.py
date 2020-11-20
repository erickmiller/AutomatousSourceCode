import unittest
import math


def closest_square_root(number):
    if number == 1:
        return number

    low = 0
    high = number

    while True:
        mid = (low + high) / 2
        mid_squared = mid ** 2

        if mid_squared == number:
            return mid
        elif low + 1 == high:
            return get_closest_number(low, high, number)
        elif mid_squared > number:
            high = mid
        else:
            low = mid


def get_closest_number(low, high, number):
    difference_from_low_sauared = math.fabs((low ** 2) - number)
    difference_from_high_squared = math.fabs((high ** 2) - number)
    if difference_from_low_sauared > difference_from_high_squared:
        return high
    else:
        return low


class ClosestSquareRootTest(unittest.TestCase):

    def test_square_root_of_one(self):
        self.assertEqual(closest_square_root(1), 1)

    def test_square_root_of_four(self):
        self.assertEqual(closest_square_root(4), 2)

    def test_square_root_of_five(self):
        self.assertEqual(closest_square_root(5), 2)

    def test_large_squares(self):
        self.assertEqual(closest_square_root(33), 6)
        self.assertEqual(closest_square_root(63), 8)
        self.assertEqual(closest_square_root(65), 8)
        self.assertEqual(closest_square_root(72), 8)
        self.assertEqual(closest_square_root(73), 9)
        self.assertEqual(closest_square_root(80), 9)


if __name__ == '__main__':
    unittest.main()
