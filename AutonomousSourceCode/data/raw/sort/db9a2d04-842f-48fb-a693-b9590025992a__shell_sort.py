def shell_sort(sort_me):
	'''
	shell_sort(list) uses shell sort algorithm to sort a list.
	It accepts a list and returns a sorted list.

	>>> my_list = shell_sort(my_list)
	'''
	gaps = [23, 16, 9, 4, 3, 2, 1]
	for gap in gaps:
		i = gap
		while i < len(sort_me):
			temp, j = sort_me[i], i
			while j >= gap and sort_me[j-gap] > temp:
				sort_me[j] = sort_me[j - gap]
				j -= gap
			sort_me[j] = temp
			i += 1
	return sort_me
