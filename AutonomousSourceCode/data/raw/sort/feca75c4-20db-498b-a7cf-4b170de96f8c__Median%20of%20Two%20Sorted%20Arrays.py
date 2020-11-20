class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        C = A + B
        C.sort()
        l = len(C)
        if l % 2 == 0:
        	return float(C[l/2] + C[l/2-1]) / 2
        else:
        	return float(C[l/2])


if __name__ == '__main__':
	s = Solution()
	a = [3,2,1,9,8]
	b = [3,6,4]
	print s.findMedianSortedArrays(a, b)
