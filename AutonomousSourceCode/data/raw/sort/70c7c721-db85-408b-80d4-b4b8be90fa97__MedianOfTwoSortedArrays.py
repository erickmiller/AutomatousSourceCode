class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        A.extend(B)
        A.sort()
        length = len(A)
        if length%2 ==0:
            return (A[length/2-1]+A[length/2])/2.0
        else:
            return A[length/2]

if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1,2,5],[3,4,6])


    raw_input()