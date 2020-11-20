"""Copyright 2013 Kawika Ohumukini.  All rights reserved.

Calculate square root of a number using Newtons method
"""

import math


def sqrt(x):
    x = float(x)
    for i in range(10):
        newtonX = x - (((x * x) - 2) / (2 * x))
        if (math.fabs(newtonX - x)) < 10**-10:
            return newtonX
        x = newtonX
    return x