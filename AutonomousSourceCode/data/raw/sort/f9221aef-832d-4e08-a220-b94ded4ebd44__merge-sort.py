#-*- coding: utf-8 -*-
def merge_sort(to_sort_list):
    if len(to_sort_list) == 1:
        return to_sort_list
    half = len(to_sort_list) / 2    
    to_sort_list[:] = merge(merge_sort(to_sort_list[:half]), merge_sort(to_sort_list[half:]))
    return to_sort_list

def merge(left_list, right_list):
    left_pos = right_pos = 0
    sorted_list = []
    while True: 
        if left_list[left_pos] < right_list[right_pos]:
            sorted_list.append(left_list[left_pos])
            left_pos = left_pos + 1
            if left_pos == len(left_list):
                sorted_list = sorted_list + right_list[right_pos:]
                break
        else:    
            sorted_list.append(right_list[right_pos])
            right_pos = right_pos + 1
            if right_pos == len(right_list):
                sorted_list = sorted_list + left_list[left_pos:]
                break
    return sorted_list        

to_sort_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(to_sort_list)
print to_sort_list
