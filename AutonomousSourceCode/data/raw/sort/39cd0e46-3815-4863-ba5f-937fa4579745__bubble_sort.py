def bubble_sort(sort_me):
	'''
	bubble_sort(list)uses bubble sort algorithm to sort a list.
	It accepts a list and returns a sorted list.

	>>> my_list = bubble_sort(my_list)
	'''
	if len(sort_me) < 2:
		return sort_me
	ocount = 1
	while ocount < len(sort_me):
		icount = 0
		while icount < len(sort_me) - ocount:
			if sort_me[icount] > sort_me[icount+1]:
				sort_me[icount], sort_me[icount+1] = sort_me[icount+1], sort_me[icount]
			icount += 1
		ocount += 1
	return sort_me
