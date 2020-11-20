''' implement merge sort
'''

''' merge two sorted arrays A and B into C
'''
import sys
def merge(A,B):
    a_len = len(A)
    b_len = len(B)
    C=[]
    A.append(sys.maxint)
    B.append(sys.maxint)
    i=j=0
    while i < a_len and j < b_len:
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
    return C


''' return a sorted array of A
'''
def merge_sort(A):
    if (len(A)==1):
        return A
    first_half = merge_sort(A[:len(A)/2])
    second_half = merge_sort(A[len(A)/2:])
    return merge(first_half, second_half)
    
    
if __name__=='__main__':
    print merge_sort([3,9,7,6,2,5,1,4])