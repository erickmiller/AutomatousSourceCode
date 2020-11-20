def slaveSort(seq):
    '''
    Given a sequence of sequences, sort all according to the
    sort order of the first sequence.
    '''
    z = list(zip(*seq))
    z.sort()
    return zip(*z)


if __name__ == '__main__':
    lists = (('cat', 'bat', 'rat'),(1,2,3),(4,5,6))
    sortedLists = slaveSort(lists)
    for l in sortedLists:
        print(l)