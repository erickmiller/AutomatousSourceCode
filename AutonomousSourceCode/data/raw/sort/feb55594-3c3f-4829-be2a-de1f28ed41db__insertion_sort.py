def insertion_sort(A):
    n = len(A)
    for j in range(2,n):
        key = A[j]
        i = j-1
        while i > 0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A
if __name__ == '__main__':
    A = [3,7,6,5,5,5,34,56]
    print "A:", A
    print "Sorted array after insertion sort", insertion_sort(A)