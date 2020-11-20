def sort(coll):
    ''' Given a collection, sort it using the bubble
    sort method (sorted by reference).

    O(n^2) performance
    O(n)   storage

    :param coll: The collection to sort
    :returns: The sorted collection
    '''
    changed = True
    indexes = range(len(coll) - 1)
    while changed:
        changed = False
        for i in indexes:
            if coll[i] > coll[i + 1]:
                coll[i], coll[i + 1] = coll[i + 1], coll[i]
                changed = True
    return coll


def sort_clone(coll):
    ''' Given a collection, sort it using the bubble
    sort method (sorted by copy).

    :param coll: The collection to sort
    :returns: The sorted collection
    '''
    return sort(list(coll))
