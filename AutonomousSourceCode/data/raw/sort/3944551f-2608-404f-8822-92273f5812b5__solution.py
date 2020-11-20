# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:19:47 2015

@author: elsa
"""


def sort_a_list(l):
    return sorted(l, reverse=True)


def sort_by_mark(l):
    return sorted(l, reverse=True)


def sort_by_name(l):
    return sorted(l, key=lambda l: l[1])
