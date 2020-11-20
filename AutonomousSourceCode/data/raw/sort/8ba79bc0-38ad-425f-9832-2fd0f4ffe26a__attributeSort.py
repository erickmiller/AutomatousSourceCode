import operator

def attributeSort(seq, attr):
    """
    """
    return sorted(seq, key=operator.attrgetter(attr))
