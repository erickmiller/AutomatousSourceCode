# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:38:13 2015

@author: MDeyell
"""


def sort_a_list(invar):
    "takes a list and return the list sorted in the descending order"
    outvar = sorted(invar, reverse=True)
    return outvar


grades = [[37, 'Jeanette Wafer'], [6, 'Joshua Tran'], [85, 'Susan Maddox']]


def sort_by_mark(grades):
    "take a list and returns it sorted by mark in the descending order"
    def getKey(item):
        return item[0]

    outvar = sorted(grades, key=getKey, reverse=True)
    return outvar


def sort_by_name(input):
    "take a list and returns it sorted by name in the ascending order"
    def getKey(item):
        return item[1]

    outvar = sorted(input, key=getKey)
    return outvar
