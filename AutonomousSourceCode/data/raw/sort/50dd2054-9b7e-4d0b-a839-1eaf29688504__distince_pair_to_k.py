__author__ = 'karthikb'

from practice.general import binary_search,merge_sort
'''
Finding all distinct pairs whose difference equal to k

a = {1, 5, 3, 4, 2}, k = 3

pairs = {1,4},{2,5}

'''
a = [1, 5, 3, 4, 2]
def solution(a, k):

    sorted_array = merge_sort(a)
    print sorted_array
    n = len(a)-1
    pairs = []
    for i in sorted_array:
        if binary_search(sorted_array,k+i,0,n) != -1:
            pairs.append((i,k+i))
    return pairs

print solution(a,3)





