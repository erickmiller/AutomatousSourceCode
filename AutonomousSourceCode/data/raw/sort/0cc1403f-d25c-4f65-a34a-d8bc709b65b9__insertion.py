def insertion_sort(list_to_sort):
    sorted_list = []
    unsorted_list = list_to_sort[:]
    while len(unsorted_list) > 0:
        selected = unsorted_list.pop()
        inserted = False
        if sorted_list == []:
            sorted_list.append(selected)
        else:
            for i in range(len(sorted_list)):
                if sorted_list[i] > selected:
                    sorted_list.insert(i, selected)
                    inserted = True
                    break
            if not inserted:
                sorted_list.append(selected)
    return sorted_list

if __name__ == '__main__':
    #best case: O(n)
    print insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9])
    #worst case: O(n^2)
    print insertion_sort([9, 8, 7, 6, 5, 4, 3, 2, 1])
