def comparator(a, b):       # compare two fractions
    if a[0] / float(a[1]) > b[0] / float(b[1]):
        return 1            # a > b
    elif a[0] / float(a[1]) == b[0] / float(b[1]):
        return 0            # a = b
    return -1               # a < b


def sort_fractions(fractions):
    return sorted(fractions, comparator)

print (sort_fractions([(2, 3), (1, 2)]))
print (sort_fractions([(2, 3), (1, 2), (1,3)]))
