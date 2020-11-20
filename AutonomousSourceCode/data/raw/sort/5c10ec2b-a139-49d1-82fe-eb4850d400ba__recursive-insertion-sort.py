__author__ = 'PyBeaner'


# n+(n-1)+(n-2)...
# O(n^2)
def recursive_insertion_sort(alist):
    length = len(alist)
    if length <= 1:
        return alist
    sorted_part = recursive_insertion_sort(alist[:-1])
    last = alist[-1]
    sorted_part.append(last)
    alist = sorted_part
    i = length - 2
    while i >= 0 and alist[i] > last:
        alist[i + 1] = alist[i]
        i -= 1
    i += 1
    alist[i] = last

    return alist


if __name__ == '__main__':
    from random import sample

    alist = sample(range(100), 20)
    alist = recursive_insertion_sort(alist)
    print(alist)
