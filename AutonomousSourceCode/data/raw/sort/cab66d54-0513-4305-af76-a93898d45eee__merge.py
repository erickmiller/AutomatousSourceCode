import sys
from heapq import merge

def internal_merge(left, right):
    ''' A helper method to merge two sorted lists

    :param left: The left sorted list to merge
    :param right: The right sorted list to merge
    :returns: The merged sorted result list
    '''
    result = []
    li, ri = 0, 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            result.append(left[li])
            li += 1
        else:
            result.append(right[ri])
            ri += 1
    if li < len(left):  result.extend(left[li:])
    if ri < len(right): result.extend(right[ri:])
    return result

def sort(coll):
    ''' Given a collection, sort it using the merge
    sort method (sorted by reference).

    O(n log n) performance
    O(n)   storage

    :param coll: The collection to sort
    :returns: The sorted collection
    '''
    if len(coll) <= 1:
        return coll
    m = len(coll) / 2
    l = sort(coll[:m])
    r = sort(coll[m:])
    return list(internal_merge(l, r))


def sort_clone(coll):
    ''' Given a collection, sort it using the bubble
    sort method (sorted by copy).

    :param coll: The collection to sort
    :returns: The sorted collection
    '''
    return sort(list(coll))
