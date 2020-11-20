#!/usr/bin/python

def merge(left, right, n):
    i = j = 0
    sorted_array = []
    for k in range(n):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

        if i == len(left):
            sorted_array.extend(right[j:])
            break
        if j == len(right):
            sorted_array.extend(left[i:])
            break

    return sorted_array


def merge_sort(A,n):
    if n <= 1: return A
    left = merge_sort(A[:n/2], n/2)
    right = merge_sort(A[n/2:], n-n/2)
    return merge(left,right, n)

def main():
    #A = [1,3,5,2,4,6]
    A = [x for x in range(1000000)]
    A.reverse()
    n = len(A)
    print '*'*50
    print 'sorted output'
    print '*'*50
    print merge_sort(A,n)


if __name__ == '__main__':
    main()
