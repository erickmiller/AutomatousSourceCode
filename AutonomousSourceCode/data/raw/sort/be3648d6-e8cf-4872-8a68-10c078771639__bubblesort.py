# Bubble Sort in Python
# (sorts a list into ascending order using "bubble sort" algorithm)


def bubble(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            greater = list[index]
            lesser = list[index + 1]
            list[index] = lesser
            list[index + 1] = greater
            
            
def is_sorted(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            return False
    return True
    
    
def bubble_sort(list):
    while not is_sorted(list):
        bubble(list)
    return list
    
    
print str(bubble_sort([9,8,7,6,5,4,3,2,1])) + "\n"


print str(bubble_sort([9,8,6,6,5,100,3,2,1])) + "\n"
