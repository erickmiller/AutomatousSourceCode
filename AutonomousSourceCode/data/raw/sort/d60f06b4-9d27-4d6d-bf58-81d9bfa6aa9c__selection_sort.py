def selection_sort(sort_me):
	'''
	selection_sort(list) uses selection sort algorithm to sort a list.
	It accepts a list and returns a sorted list.

	>>> my_list = selection_sort(my_list)
	'''
	ocount = 0
	while ocount < len(sort_me)-1:
		lpos = icount = ocount
		while icount < len(sort_me):
			if sort_me[icount] < sort_me[lpos]:
				lpos = icount
			icount += 1
		sort_me[lpos], sort_me[ocount] = sort_me[ocount], sort_me[lpos]
		ocount += 1
	return sort_me
