from operator import itemgetter, attrgetter


def sort_a_list(l):
    a = (sorted(l, reverse=True))
    return(a)


def sort_by_mark(my_class):
    b = (sorted(my_class, reverse=True))
    return(b)


def sort_by_name(my_class):
    getcount = itemgetter(1)
    c = (sorted(my_class, key=getcount))
    return(c)
