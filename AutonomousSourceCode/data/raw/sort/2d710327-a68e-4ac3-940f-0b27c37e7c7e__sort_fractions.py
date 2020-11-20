def getKey(item):
    return item[0] / item[1]


def sort_fractions(fractions):
    return sorted(fractions, key=getKey)


print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
