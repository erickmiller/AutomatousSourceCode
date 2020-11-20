import merge
def merge_sort(alist):
	""" (list of number) -> (list of number sorted)

	Return a list of number sorted use O(nlogn) time

	>>> merge_sort([1, 3 ,2, 7, 4, 6])
	[1, 2, 3, 4, 6, 7]
	"""

	n = len(alist)

	if n == 0 or n == 1:
		return alist
	else:
		leftList = alist[:n/2]
		rightList = alist[n/2:]

		leftSorted = merge_sort(leftList)
		rightSorted = merge_sort(rightList)

		return merge.merge(leftSorted, rightSorted)

# if __name__ == '__main__':
# 	print(merge_sort([1, 3 ,2, 7, 4, 56]))

