def sort(coll):
    ''' Given a collection, sort it using the insertion
    sort method (sorted by reference).

    O(n^2) performance
    O(n)   storage

    :param coll: The collection to sort
    :returns: The sorted collection
    '''
    for j in range(1, len(coll)):
        k = coll[j]
        i = j - 1
        while i > 0 and coll[i] > k:
            coll[i + 1] = coll[i]
            i = i - 1
        coll[i + 1] = k
    return coll


def sort_clone(coll):
    ''' Given a collection, sort it using the insertion
    sort method (sorted by copy).

    :param coll: The collection to sort
    :returns: The sorted collection
    '''
    return sort(list(coll))
