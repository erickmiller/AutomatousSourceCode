def median(lst):
    # sort list in ascending order
    sorted_lst = sorted(lst)      
    # obtain list length
    lst_length = len(sorted_lst)
    
    # list has even num of elements
    if lst_length % 2 == 0:
        index_1 = lst_length / 2
        index_2 = index_1 - 1
        median = (sorted_lst[index_1] + sorted_lst[index_2]) / 2.0
        return median   
    # list has odd num of elements
    elif lst_length % 2 == 1:
        median = 0
        index = lst_length / 2
        median = sorted_lst[index]
        return median