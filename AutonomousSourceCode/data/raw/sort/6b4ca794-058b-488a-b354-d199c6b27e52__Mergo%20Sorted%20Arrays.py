class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        j=0
        for i in range(m,m+n):
            A[i]=B[j]
            j+=1
            if j==n:
                break
        A.sort()
        return A
