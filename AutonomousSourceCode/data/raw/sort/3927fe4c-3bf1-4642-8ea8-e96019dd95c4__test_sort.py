""" Speed performance tests.

    Copyright (c) 2014, eGenix.com Software GmbH; mailto:info@egenix.com
    See the documentation for further information on copyrights,
    or contact the author. All Rights Reserved.

    License: MIT

"""
import operator

loops = range(1000)

### Sorting tuples

seq1 = loops[:]
seq2 = loops[:]
seq2.reverse()
seq = zip(seq1, seq2)
result = zip(seq2, seq1)

def list_sort_method():

    l = result[:]
    l.sort()
    return l

assert list_sort_method() == seq

def list_sorted():

    l = sorted(result)
    return l

assert list_sorted() == seq

def decorate_sort():

    dl = [(x[1], x) for x in seq]
    dl.sort()
    l = [b for a, b in dl]
    return l

assert decorate_sort() == result

def decorate_sort_generators():

    l = [x for (item, x) in sorted((x[1], x) for x in seq)]
    # using indexing is slightly slower:
    #l = [y[1] for y in sorted((x[1], x) for x in seq)]
    return l

assert decorate_sort_generators() == result

def key_lambda_sort():
    l = seq[:]
    l.sort(key=lambda x: x[1])
    return l
   
assert key_lambda_sort() == result
    
def key_itemgetter_sort():
    l = seq[:]
    l.sort(key=operator.itemgetter(1))
    return l
   
assert key_itemgetter_sort() == result

### Sorting objects

class Data:
    a = 1
    b = 2
    def __init__(self, a, b):
        self.a = a
        self.b = b
obj_seq = [Data(seq[i][0], seq[i][1]) for i in loops]

# Decorate/sort/undecorate pattern:
obj_result = [d for (i, d) in sorted((d.b, d) for d in obj_seq)]

def key_lambda_attribute_sort():
    l = obj_seq[:]
    l.sort(key=lambda x: x.b)
    return l
   
assert key_lambda_attribute_sort() == obj_result
    
def key_attrgetter_attribute_sort():
    l = obj_seq[:]
    l.sort(key=operator.attrgetter('b'))
    return l
   
assert key_attrgetter_attribute_sort() == obj_result

###

if __name__ == '__main__':
    import perftools
    perftools.time_functions(globals())
