#!/usr/bin/env python

def merge_sort(in_list):
    
    l_len = len(in_list)

    if l_len == 1:
        return in_list
    
    h_len = len(in_list)/2
    h1 = merge_sort(in_list[:h_len])
    h2 = merge_sort(in_list[h_len:])

    #print h1, h2
    sorted_list = []

    while (len(h1) + len(h2)) != 0:
        if h1 == []:
            return sorted_list + h2
        elif h2 == []:
            return sorted_list + h1
        elif h1[0] < h2[0]:
            sorted_list.append(h1.pop(0))
        else:
            sorted_list.append(h2.pop(0))

    return sorted_list

in_list = [33,6,43,32,63,66,3,45,8,201,98,78,98,23,43,12,36,72,17,1]

print merge_sort(in_list)
