def sort_fractions(fractions):
    return sorted(fractions, key=getKey)


def getKey(item):
    return item[0]/item[1]
