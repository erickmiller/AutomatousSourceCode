def merge_sort(sort_me):
	'''
	merge_sort(list) uses merge sort algorithm to sort a list.
	It accepts a list and returns a sorted list.

	>>> my_list = merge_sort(my_list)
	'''
	if len(sort_me) < 2:
		return sort_me
	mid = int(len(sort_me)/2)
	lower = merge_sort(sort_me[:mid])
	upper = merge_sort(sort_me[mid:])
	merge = []

	i, j = 0, 0
	while i < len(lower) and j < len(upper):
		if lower[i] <= upper[j]:
			merge.append(lower[i])
			i += 1
		else:
			merge.append(upper[j])
			j += 1
	merge += lower[i:]
	merge += upper[j:]
	return merge
