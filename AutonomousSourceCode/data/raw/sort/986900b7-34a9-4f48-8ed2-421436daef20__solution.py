# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:39:40 2015

@author: simonfredon
"""


from operator import *


def sort_a_list(lista):
    a = sorted(lista, reverse=True)
    return a


def sort_by_mark(mycl):
    b = sorted(mycl, key=itemgetter(0), reverse=True)
    return b


def sort_by_name(mclass):
    c = sorted(mclass, key=itemgetter(1))
    return c
