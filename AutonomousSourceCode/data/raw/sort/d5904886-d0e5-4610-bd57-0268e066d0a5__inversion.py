import timeit

num_inversions = 0
def split(number_array):
    array_length = len(number_array)
    first_half = number_array[0:array_length/2]
    second_half = number_array[array_length/2::]
    return first_half, second_half 

def sort_and_count_inversions(number_array):
    array_length = len(number_array)
    if array_length == 1:
        return number_array, 0
    else:
        first_half, second_half = split(number_array)
        sorted_first_half, first_half_inversions = sort_and_count_inversions(first_half)
        sorted_second_half, second_half_inversions = sort_and_count_inversions(second_half)
        merged_array, merge_inversions = merge_and_count_split_inversions(sorted_first_half,
                sorted_second_half)
    return merged_array, first_half_inversions + second_half_inversions + merge_inversions

def merge_and_count_split_inversions(sorted_left_array, sorted_right_array):
    sorted_array = []
    split_inversions = 0
    while len(sorted_left_array) > 0 or len(sorted_right_array) > 0:
        if len(sorted_right_array) == 0: 
            sorted_array.append(sorted_left_array.pop(0))
        elif len(sorted_left_array) == 0:
            sorted_array.append(sorted_right_array.pop(0))
        elif int(sorted_left_array[0]) < int(sorted_right_array[0]):
            sorted_array.append(sorted_left_array.pop(0))
        else:
            sorted_array.append(sorted_right_array.pop(0))
            split_inversions += len(sorted_left_array)
    return sorted_array, split_inversions       

# you can use this to test the difference in execution time
def brute_force(array):
    inversions = 0
    while len(array) > 0:
        first_item = array.pop(0)
        for item in array:
            if int(item) > int(first_item):
                inversions += 1
    return inversions

with open('IntegerList.txt') as f:
   large_array = f.readlines()
   sorted_array, inversions = sort_and_count_inversions(large_array)
   for item in sorted_array:
       print item
   print 'The # of inversions is: ', inversions
        #inversions = count_inversions(large_array)
        #sorted_left_array = sort(left_array)
        #sorted_right_array = sort(right_array)
        #sorted_array = merge(sorted_left_array, sorted_right_array)

