# An implementation of the selection sort algorithm in Python.




def find_minimum_with_index(list):
    candidate = list[0]
    candidate_index = 0
    for index in range(1, len(list)):
        if list[index] < candidate:
             candidate = list[index]
             candidate_index = index
    return [candidate, candidate_index]
    
    
def selection_sort(list):
    sorted_list = []
    for index in range(len(list)):
        minimum_index = find_minimum_with_index(list)[1]
        sorted_list.append(list.pop(minimum_index))
    return sorted_list
    
    
    
print str(selection_sort([9,8,7,6,5,4,3,2,1])) + "\n"

print str(selection_sort([9,8,6,6,5,100,3,2,1])) + "\n"

    