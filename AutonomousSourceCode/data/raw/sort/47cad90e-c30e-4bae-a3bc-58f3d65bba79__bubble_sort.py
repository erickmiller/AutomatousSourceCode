#This program manually sorts a list of numbers.

def bubble_sort(my_list):
    sorted = False
    while sorted == False:
        previous = my_list[0]
        sorted = True
        for index in range(len(my_list)):
            if previous > my_list[index]:
                my_list[index], my_list[index - 1] = previous, my_list[index]
                sorted = False
            else:
                previous = my_list[index]
    return my_list

assert [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2])
assert [1, 4, 5] == bubble_sort([4, 5, 1])
assert [1, 1, 1] == bubble_sort([1, 1, 1])
assert [2] == bubble_sort([2])
