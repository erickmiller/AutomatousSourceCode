#!/usr/bin/env python

import random

lesserSort = sorted

def sorted(list, key=None):
    '''
    Perform an in-place sort on list.
    '''
    if random.random() < 0.5:
        while True:
            random.shuffle(list)
            if list == lesserSort(list, key=key):
                return list
    else:
        return lesserSort(list, key=key)
