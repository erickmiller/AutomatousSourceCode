def odd_even_sort(in_array):
    is_sorted = False
    length=len(in_array)-1
    (even_loop, odd_loop) = (range(1,length, 2), range(0, length, 2))

    while not is_sorted:
        is_sorted = True
        if not sorted_loop(even_loop, in_array):
            is_sorted = False
        if not sorted_loop(odd_loop, in_array):
            is_sorted = False
    return in_array

def sorted_loop(loop, in_array):
    is_sorted = True
    for i in loop:
        if in_array[i] > in_array[i+1]:
            in_array[i], in_array[i+1] = in_array[i+1], in_array[i]
            is_sorted = False
    return is_sorted

