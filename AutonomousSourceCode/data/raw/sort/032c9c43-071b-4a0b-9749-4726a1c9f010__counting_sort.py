#!/usr/bin/python2

def counting_sort(A, k):
    C = [0] * k
    B = [None] * len(A)
    for a in A:
        C[a] += 1 
    for i in range(1, len(C)):
        C[i] = C[i-1] + C[i]
    for a in reversed(A):
        B[C[a]-1] = a
        C[a] -= 1
    return B


if __name__ == "__main__":

    A = [2, 5, 3, 0, 2, 3, 0, 3]
    B = counting_sort(A, 6)
    print "Sorted %r" % B
