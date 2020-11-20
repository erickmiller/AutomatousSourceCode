def merge_sort(input_array):
    length_of_input = len(input_array)
    if length_of_input == 1:
        return input_array
    else:
        first_sorted_half = merge_sort(input_array[0 : int(length_of_input / 2)])
        second_sorted_half = merge_sort(input_array[int(length_of_input / 2): ])
        sorted_array = merge(first_sorted_half, second_sorted_half)
        return sorted_array

def merge(first_sorted_array, second_sorted_array):
    length_1 = len(first_sorted_array)
    length_2 = len(second_sorted_array)
    total_length = length_1 + length_2

    i = 0
    j = 0
    merged_array = []

    for idx in range(total_length):

        if first_sorted_array[i] > second_sorted_array[j]:
            merged_array.append(second_sorted_array[j])
            j += 1
        else:
            merged_array.append(first_sorted_array[i])
            i += 1

        if i == length_1:
            merged_array += second_sorted_array[j : ]
            return merged_array
        elif j == length_2:
            merged_array += first_sorted_array[i : ]
            return merged_array
