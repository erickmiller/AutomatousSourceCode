
def comparator(a, b):       # compare two fractions
    if a[0] / float(a[1]) > b[0] / float(b[1]):
        return 1            # a > b
    elif a[0] / float(a[1]) == b[0] / float(b[1]):
        if a[0] > b[0]:
            return 1        # a > b
        elif a[0] == b[0]:
            return 0        # a == b
        else:
            return -1       # a < b
    return -1               # a < b


def sort_fractions(fractions):
    return sorted(fractions, comparator)
