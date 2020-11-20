def sort_a_list(L):
    M = sorted(L, reverse=True)
    return(M)

import operator


def sort_by_mark(myclass):
    myclass = sorted(myclass, key=operator.itemgetter(0), reverse=True)
    return(myclass)


def sort_by_name(myclass):
    myclass = sorted(myclass, key=operator.itemgetter(1))
    return(myclass)
