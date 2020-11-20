import operator


def sort_a_list(l):
    return sorted(l, reverse=True)


def sort_by_mark(my_class):
    return sorted(my_class, key=operator.itemgetter(0), reverse=True)


def sort_by_name(my_class):
    return sorted(my_class, key=operator.itemgetter(1))
