def sort_a_list(L):
    V = sorted(L, reverse=True)
    return(V)


from operator import itemgetter


def sort_by_mark(Y):
    P = sorted(Y, key=itemgetter(0), reverse=True)
    return(P)


def sort_by_name(B):
    S = sorted(B, key=itemgetter(1))
    return(S)
