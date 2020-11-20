import numpy as np
def sort_from_indexes(ind_l,l):
    l_sorted=[]
    for i in range (0,len(ind_l)):
        l_sorted.append(l[ind_l[i]])
    return l_sorted
