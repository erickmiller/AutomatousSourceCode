import pytest
import math
from pybelsberg import always


def test_sqrt(Point, almost):
    a = Point(0.0, 10.0)

    @always
    def constraint_square_root():
        #XXX Z3 returns -1 for a.x if not squared
        return math.sqrt(a.x ** 2) == 10

    assert almost(abs(a.x), 10)


def test_sum(Point):
    a = Point(0, 10)
    b = Point(20, 30)
    c = Point(40, 50)

    @always
    def constraint_sum_over_500():
        return sum([a.x, a.y, b.x, b.y, c.x, c.y]) > 500

    assert a.x + a.y + b.x + b.y + c.x + c.y > 500
