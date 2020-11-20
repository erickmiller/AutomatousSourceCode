# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:53:03 2015

@author: xavierduportet
"""
import operator


def sort_a_list(l):
    return sorted(l, reverse=True)


def sort_by_mark(my_class):
    mark = operator.itemgetter(0)
    return sorted(my_class, key=mark, reverse=True)


def sort_by_name(my_class):
    name = operator.itemgetter(1)
    return sorted(my_class, key=name)
