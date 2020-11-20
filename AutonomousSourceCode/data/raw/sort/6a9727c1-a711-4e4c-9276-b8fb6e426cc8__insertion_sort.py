def insertion_sort(the_list, sorted_length = 0):
    if len(the_list) <= sorted_length:
        return the_list
    current = the_list.pop()
    if sorted_length == 0:
        the_list.insert(0,current)
    else:
        for x in range(sorted_length):
            if the_list[x] >= current:
                the_list.insert(x, current)
                return insertion_sort(the_list, sorted_length + 1)
        the_list.insert(sorted_length,current)
    return insertion_sort(the_list, sorted_length + 1)


a = [3,2,4,5,19,20,2,30,1000,1]
print a
insertion_sort(a)
print a
a.sort()
print a
