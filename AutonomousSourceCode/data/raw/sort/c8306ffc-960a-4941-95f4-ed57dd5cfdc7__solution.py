from operator import itemgetter


def sort_a_list(l):
    a = sorted(l, reverse=True)
    return(a)


def sort_by_mark(my_class):
    a = sorted(my_class, reverse=True)
    return(a)


def sort_by_name(my_class):
    getcount = itemgetter(1)
    a = sorted(my_class, key=getcount)
    return(a)
