# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:56:59 2015

@author: pippo
"""
from operator import *


def sort_a_list(lista):
    stampa = sorted(lista, reverse=True)
    return stampa


def sort_by_mark(mycl):
    stampi = sorted(mycl, key=itemgetter(0), reverse=True)
    return stampi


def sort_by_name(mclass):
    stampo = sorted(mclass, key=itemgetter(1))
    return stampo
