# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from operator import itemgetter


def sort_a_list(l):
    return sorted(l, reverse=True)


def sort_by_mark(my_class):
    return sorted(my_class, reverse=True)


def sort_by_name(my_class):
    return sorted(my_class, key=itemgetter(1))
