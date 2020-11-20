import operator


def sort_a_list(l):
    return sorted(l, reverse=True)


def sort_by_mark(l):
    return sorted(list(l), reverse=True)


def sort_by_name(l):
    return sorted(list(l), key=operator.itemgetter(1), reverse=False)
