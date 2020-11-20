def insertion_sort(sort_me):
	'''
	insertion_sort(list) uses insertion sort algorithm to sort a list.
	It accepts a list and returns a sorted list.

	>>> my_list = insertion_sort(my_list)
	'''
	ocount = 1
	while ocount < len(sort_me):
		icount = ocount - 1
		val = sort_me[ocount]
		while icount >= 0:
			if sort_me[icount] > val:
				sort_me[icount+1] = sort_me[icount]
			else:
				break
			icount -= 1
		sort_me[icount+1] = val
		ocount += 1
	return sort_me
