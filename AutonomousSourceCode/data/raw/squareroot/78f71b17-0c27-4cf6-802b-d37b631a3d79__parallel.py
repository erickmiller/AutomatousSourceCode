import unittest
from os.path import dirname, join, abspath
import sys

here = lambda *args: join(abspath(dirname(__file__)), *args)
root = here("..", "..")
sys.path.append(root)

from tvshowhelper.parallel import parallel_map


class TestParallel(unittest.TestCase):

    def test_map(self):
        def _square(x):
            return x + 1

        numbers = range(1000)
        squared_numbers = map(_square, numbers)
        results = parallel_map(_square, numbers, 500)
        self.assertTrue(results == squared_numbers)

if __name__ == '__main__':
    unittest.main()
