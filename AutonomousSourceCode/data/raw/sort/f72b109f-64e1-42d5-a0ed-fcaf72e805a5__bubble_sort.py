from create_list import random_list, is_sorted


def bubble_sort(my_list):
    """
    Perform bubble sort on my_list.
    """
    while not is_sorted(my_list):
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list

my_list = random_list(50)
print(my_list)
print(is_sorted(my_list))

sorted_list = bubble_sort(my_list)
print(sorted_list)
print(is_sorted(sorted_list))
