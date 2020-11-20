# Algorithm course by Stanford on Coursera

# Merge sort
# Given a list of unsorted numbers, sort them
# in ascending order using merge-sort algorithm

import random
import time


def build_random_list(upper_limit):
    rand_list = list(range(1, upper_limit))
    random.shuffle(rand_list)
    #print(rand_list)
    return rand_list


def merge_sort(rand_list):
    if len(rand_list) == 1:
        return rand_list

    half_len = int(len(rand_list) / 2)
    sec_half = len(rand_list) - half_len

    left_list = rand_list[:half_len]
    right_list = rand_list[half_len:]

    left_sorted = merge_sort(left_list)
    right_sorted = merge_sort(right_list)

    # combine sorted results
    sorted_list = list()
    i = 0
    j = 0
    for k in range(len(rand_list)):
        if i == len(left_sorted):
            while j < len(right_sorted):
                sorted_list.append(right_sorted[j])
                j += 1
            break

        if j == len(right_sorted):
            while i < len(left_sorted):
                sorted_list.append(left_sorted[i])
                i += 1
            break
                          
        # 
        if left_sorted[i] <= right_sorted[j]:
            sorted_list.append(left_sorted[i])
            i += 1
        else:
            sorted_list.append(right_sorted[j])
            j += 1

    return sorted_list


def calc_running_time(MS=False, upper_limit=1E3, num_trials=1E3):
    # start time
    time_start = time.time()
    
    for i in range(num_trials):
        rand_list = build_random_list(upper_limit)
        #print(rand_list)

        if MS:
            sorted_list = merge_sort(rand_list)
        #print(sorted_list)

        else:
            rand_list.sort()

    # end time
    time_end = time.time()
    # elapsed time
    time_spent = time_end - time_start
    
    return time_spent


def test_merge_sort():
    error_count = 0
    upper_limit = int(1E2)

    for i in range(1000):
        rand_list = build_random_list(upper_limit)
        #print(rand_list)

        sorted_list = merge_sort(rand_list)
        #print(sorted_list)

        rand_list.sort()
        if sorted_list != rand_list:
            #print('Error: merge sort implemention incorrect.', upper_limit)
            #print(rand_list)
            error_count += 1

    print('Number of errors in merge sort is ', error_count)        
        
    
#
# test_merge_sort()


for i in range(2, 10):
    upper_limit = int(10**i)
    print('Size of list: ', upper_limit)
    num_trials = 1000
    
    regular_RT = calc_running_time(False, upper_limit, num_trials)
    print('Python sort running time: ', regular_RT)
    
    MS_RT = calc_running_time(True, upper_limit, num_trials)
    print('Merge sort running time: ',MS_RT)

quit() 

# results
#
Size of list:  100
Python sort running time:  0.08988785743713379
Merge sort running time:  0.5029749870300293
Size of list:  1000
Python sort running time:  0.9489920139312744
Merge sort running time:  6.389283895492554
Size of list:  10000
Python sort running time:  10.525191068649292
Merge sort running time:  79.75374698638916
