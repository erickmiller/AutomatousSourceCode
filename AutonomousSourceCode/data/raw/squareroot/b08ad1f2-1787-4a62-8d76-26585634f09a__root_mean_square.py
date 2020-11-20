"""
The root mean square (abbreviated RMS or rms), also known as the quadratic mean, in statistics is a statistical measure
defined as the square root of the mean of the squares of a sample. RMS can also be calculated for a continuously varying
function.
In physics it is a characteristic of a continuously varying quantity, such as a cyclically alternating electric current,
obtained by taking the mean of the squares of the instantaneous values during a cycle.
"""

import math

__author__ = "paulogp"
__copyright__ = "Copyright (C) 2015 Paulo G.P."
__date__ = "23/11/2015"


def sin_rms(a):
    """
    The root mean square of a sine wave.
    y = a sin(2 pi f t)
    :param a: amplitude (peak value)
    :return: float
    """
    return a / math.sqrt(2)


def square_rms(a):
    """
    The root mean square of a square wave.
    y = a if ft < 0.5 V -a if ft > 0.5
    :param a: amplitude (peak value)
    :return: float
    """
    return a


def triangle_rms(a):
    """
    The root mean square of a triangle wave.
    y = |2 a ft - a|
    :param a: amplitude (peak value)
    :return: float
    """
    return a / math.sqrt(3)


def eng_rms(rms_ac, rms_dc):
    """
    The root mean square of a non sine wave.
    y = |2 a ft - a|
    :param rms_ac: ac rms
    :param rms_dc: dc rms
    :return: float
    """
    return math.sqrt(math.pow(rms_dc, 2) + math.pow(rms_ac, 2))

if __name__ == "__main__":
    print("Sine Wave RMS: {0}.".format(round(sin_rms(500.00), 2)))
    print("Square Wave RMS: {0}.".format(round(square_rms(500.00), 2)))
    print("Triangle Wave RMS: {0}.".format(round(triangle_rms(500.00), 2)))
    print("RMS total: {0}.".format(round(eng_rms(220.00, 120.00), 2)))
