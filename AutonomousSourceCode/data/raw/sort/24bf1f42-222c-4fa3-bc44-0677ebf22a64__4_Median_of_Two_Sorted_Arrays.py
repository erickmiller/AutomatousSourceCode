"""
Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        C = A
        C.extend(B)
        C.sort()
        length = len(C)
        if len(C)%2 == 1:
            return C[len(C)/2]
        else:
            return float(C[length/2]+C[length/2-1])/2