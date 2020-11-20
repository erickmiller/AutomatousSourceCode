__author__ = 'relic'


def merge_sort(a):
    """
    :param a: a list of numbers
    :return: a new sorted list of numbers those come from param a and without a be sorted
    """
    length = len(a)
    if length < 2:
        return a
    mid = length // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    a = merge(left, right)
    return a
    

def merge(a, b):
    """
    :param a: a sorted list of numbers
    :param b: a sorted list of numbers
    :return: a sorted list of numbers those from param a and b
    """
    ans = []
    while a and b:
        if a[0] > b[0]:
            ans.append(b.pop(0))
        else:
            ans.append(a.pop(0))
    ans.extend(a + b)
    return ans