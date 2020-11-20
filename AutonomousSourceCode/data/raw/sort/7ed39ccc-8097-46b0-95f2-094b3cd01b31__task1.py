#!/bin/env python

"""
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""
l = [5,2,1,5,9,10,11]
l2 = [4, 8]

def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    elif len(my_list) == 2:
        temp_list = []
        if my_list[0] > my_list[1]:
            temp_list.append(my_list[0])
            temp_list.append(my_list[1])
        else: 
            temp_list.append(my_list[1])
            temp_list.append(my_list[0])
        return temp_list
    else:
        temp_list = []
        list1 = my_list[:(len(my_list)-1)/2]
        list2 = my_list[(len(my_list)-1)/2:]
        sorted_list1 = merge_sort(list1)
        sorted_list2 = merge_sort(list2)
        while len(sorted_list1) != 0 and len(sorted_list2) != 0:
            if sorted_list1[0] > sorted_list2[0]:
                temp_list.append(sorted_list1.pop(0))
            else: 
                temp_list.append(sorted_list2.pop(0))
        if len(sorted_list1) == 1 and len(sorted_list2) == 0:
            temp_list.append(sorted_list1.pop(0))
        elif len(sorted_list1) == 0 and len(sorted_list2) == 1:
            temp_list.append(sorted_list2.pop(0))
        return temp_list




sorted_l = merge_sort(l)
print sorted_l


