"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """   
    non_zero_el = sort_line(line)[1]
    sorted_line = sort_line(line)[0]
    # merges two adjacent equal elements
    for index in range(non_zero_el - 1):
        if (sorted_line[index] == sorted_line[index + 1]) and (sorted_line[index]):
            sorted_line[index] = sorted_line[index] * 2
            sorted_line[index + 1] = 0
        else:
            sorted_line[index] = sorted_line[index]    
    
    return sort_line(sorted_line)[0]


def sort_line(a_list):
    """
    Function that shifts all non-zero elements to the left
    """
    index = 0
    a_zerolist = [0] * len(a_list)
    for element in a_list:
        if element:
            a_zerolist[index] = element
            index += 1        
    return a_zerolist, index
   
print merge([2, 2, 2, 2, 2])