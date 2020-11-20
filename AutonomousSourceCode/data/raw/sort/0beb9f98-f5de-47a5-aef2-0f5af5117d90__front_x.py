def front_x(words):
    x_list =[]
    non_x_list = []
    sorted_list = []
    for str in words:
        if str[0].lower().startswith("x"):
            x_list.append(str)
        else:
            non_x_list.append(str)
    print x_list,
    print non_x_list
    print type(x_list)
    
    print sorted(x_list)
    print type(sorted(x_list))
    
    sorted_list = sorted(x_list)+sorted(non_x_list)
            
  # +++your code here+++
    return sorted_list


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
  # +++your code
    sort_by = []
    for item in tuples:
        sort_by.append(item[-1])
    sorted_index = sorted(sort_by)
        
    print sorted_index
    return sorted_index
