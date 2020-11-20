# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:33:36 2015

@author: A
"""


def sort_a_list(liste):
    liste.sort()
    liste.reverse()
    return liste


def sort_by_mark(liste2):
    # zz = list(map(operator.itemgetter(0),liste))
    # liste2 = sorted(liste2, key=lambda liste2: liste2[0], reverse=True)
    liste2.sort(key=lambda liste2: liste2[0], reverse=True)
    return liste2


def sort_by_name(liste2):
    # sorted(liste2, key=lambda liste2: liste2[1])
    liste2.sort(key=lambda liste2: liste2[1])
    return liste2
