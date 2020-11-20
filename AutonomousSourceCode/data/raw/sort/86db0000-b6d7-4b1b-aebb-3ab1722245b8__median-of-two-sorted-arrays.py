# http://oj.leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
	# @return a float
	def findMedianSortedArrays(self, A, B):
		c = A + B
		c.sort()
		ln = len(c)
		if ln % 2 == 0:
			return (c[ln / 2 - 1] + c[ln / 2]) / 2.0
		else:
			return c[ln / 2]
