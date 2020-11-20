__author__ = 'VGN'


def merge(a, b):
    """
    Merge subroutine to merge the sorted lists a and b
    :param a: sorted subarray a
    :param b: sorted subarray b
    :return: new list merging the sorted list a and b
    """
    c = list()
    i = 0
    j = 0
    #condition to check if i and j pointers dont fall off
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i = i+1
        elif b[j] < a[i]:
            c.append(b[j])
            j = j+1
    if i < len(a):
        for k in range(i, len(a)):
            c.append(a[k])
    if j < len(b):
        for k in range(j, len(b)):
            c.append(b[k])
    return c


def merge_sort(input):
    length = len(input)
    if length <= 1:
        return input
    a = merge_sort(input[0:length/2])
    b = merge_sort(input[length/2:])
    return merge(a, b)

