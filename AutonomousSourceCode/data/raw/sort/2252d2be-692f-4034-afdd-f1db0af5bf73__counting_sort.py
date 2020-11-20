'''
In this module we implement counting sort

'''


def counting_sort(arr):
    '''
    Sort array using counting sort

    '''
    count = [0] * (max(arr)+1)
    sorted_list = [0]*len(arr)
    for i in arr:
        count[i] += 1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for i in arr:
        sorted_list[count[i] - 1] = i
        count[i] -= 1
    return sorted_list    