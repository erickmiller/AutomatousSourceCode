def sort_a_list(a):
    OK = False
    while OK is False:
        OK = True
        for i in range(0, len(a) - 1):
            if a[i] < a[i + 1]:
                tmp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = tmp
                OK = False
    return(a)


def sort_by_mark(a):
    b = sorted(a, reverse=True)
    return(b)


def sort_by_name(a):
    from operator import itemgetter, attrgetter
    c = itemgetter(1)
    b = sorted(a, key=c)
    return(b)
