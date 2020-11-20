#!/usr/bin/env python3
# -*- coding: utf-8 -*-
numbers = [25, 72, -35, 10, -34, -91, 2, -2]	#[.....-2, 2]
print(numbers)
print(sorted(numbers))
print(sorted(numbers, key = abs))		# keep original order if same value
print(sorted(numbers, key = lambda x: x % 10))

words = ['bob', 'Haha', 'WTO', 'Lily', 'isRight', 'P']
print(words)
print(sorted(words))
print(sorted(words, reverse = True))
print(sorted(words, reverse = True, key = str.lower))	#reverse&key position don't matter

record = [('Bob', 75), ('Lily', 93), ('dike', 88), ('Lisa', 82)]
def sortByName(rec):
    return rec[0].lower()
print(sorted(record, key = sortByName))
from operator import itemgetter
print(sorted(record, key = itemgetter(0)))
print(sorted(record, key = lambda record:record[1], reverse = True))