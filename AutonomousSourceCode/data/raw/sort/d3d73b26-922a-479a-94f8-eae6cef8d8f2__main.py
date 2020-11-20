__author__ = 'abdelrahman'

arr = []

def merge(a, b):
    c = []
    while a and b:
        if a[0] < b[0]:
            c += [a[0]]
            a = a[1: len(a)]
        else:
            c += [b[0]]
            b = b[1: len(b)]
    if a:
        c += a
    else:
        c += b
    return c


def merge_sort(arr):
    if len(arr) == 1:
        return [arr[0]]
    a1 = merge_sort(arr[0: len(arr)/2])
    a2 = merge_sort(arr[len(arr)/2:len(arr)])
    return merge(a1, a2)


with open('rosalind_ms.txt') as f:
    n = int(f.readline())
    arr = f.readline().split()
    arr = map(int, arr)

sorted_arr = merge_sort(arr)
sorted_arr = map(str, sorted_arr)
print(' '.join(sorted_arr))