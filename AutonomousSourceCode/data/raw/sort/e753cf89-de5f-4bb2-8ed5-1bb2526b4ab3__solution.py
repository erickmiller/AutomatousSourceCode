def sort_a_list(a):
    b = sorted(a, reverse=True)
    return(b)


def sort_by_mark(c):
    import operator
    d = sorted(c, key=operator.itemgetter(0), reverse=True)
    return(d)


def sort_by_name(e):
    import operator
    f = sorted(e, key=operator.itemgetter(1))
    return(f)
