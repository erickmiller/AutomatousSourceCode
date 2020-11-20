"""
    Look through the list.  Find the smallest element.  Swap it to the front.
    Repeat.
"""
l = [1,3,5,2,8,7,9,6]

def swapItems(local_list, index1, index2):
    index1
    index2
    hold = local_list[index1]
    local_list[index1] = local_list[index2]
    local_list[index2] = hold
    return local_list

def sortList(org_list):

    sorted_list = org_list

    for i in range(0, len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            if sorted_list[j] < sorted_list[i]:
                swapItems(sorted_list, j, i)

    return sorted_list

print(sortList(l))
