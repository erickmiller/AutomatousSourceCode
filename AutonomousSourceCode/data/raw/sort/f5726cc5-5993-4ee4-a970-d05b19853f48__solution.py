def sort_a_list(l):
    return sorted(l, reverse=True)


from operator import itemgetter


def sort_by_mark(my_class):
    return sorted(my_class, key=itemgetter(0), reverse=True)

from operator import itemgetter


def sort_by_name(my_class):
    return sorted(my_class, key=itemgetter(1))
