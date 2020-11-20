# Merge Sorted Array II
# Merge two given sorted integer array A and B into a new sorted integer array.
#
# Example
# A=[1,2,3,4]
# B=[2,4,5,6]
# return [1,2,2,3,4,4,5,6]
#


class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array

    # Merge Sort
    def mergeSortedArray(self, A, B):
        if len(A) == 0:
            return B
        if len(B) == 0:
            return A
        
        result = []
        i,j = 0,0
        while (i < len(A)) and (j < len(B)):
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
        
        if i == len(A):
            result += B[j:]
        if j == len(B):
            result += A[i:]
            
        return result



    # Easy Way
    def mergeSortedArray(self, A, B):
        C = A + B
        C.sort()
        return C
