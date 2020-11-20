#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__Version__ = '0.0.1'
__Author__ = 'aQua'
__License__ = 'MIT'

# -----------------------------------------------------
# Date: 2015/4/12
# Description:
# -----------------------------------------------------
from sicp_p46_fixed_point import fixed_point


def average_damp(f):
    return lambda x: (x + f(x)) / 2


def square(x):
    return x * x


print(average_damp(square)(10))


def cube_root(x):
    return fixed_point(average_damp(lambda y: x / square(y)), 1)

print(cube_root(27))