def sort_a_list(l):
    u = sorted(l)
    return(u[::-1])


def sort_by_mark(my_class):
    u = sorted(my_class, reverse=True)
    return(u)


def sort_by_name(my_class):
    from operator import itemgetter, attrgetter
    c = itemgetter(1)
    u = sorted(my_class, key=c)
    return(u)
