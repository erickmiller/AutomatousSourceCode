def comb_sort(sort_me):
	'''
	comb_sort(list) uses comb sort algorithm to sort a list.
	It accepts a list and returns a sorted list.

	>>> my_list = comb_sort(my_list)
	'''
	gap = len(sort_me)

	while gap > 1 or swapped:
		gap = int(gap / 1.3)
		if gap < 1:
			gap = 1
		i = 0
		swapped = False
		while i + gap < len(sort_me):
			if sort_me[i] > sort_me[i+gap]:
				sort_me[i], sort_me[i+gap] = sort_me[i+gap], sort_me[i]
				swapped = True
			i += 1
	return sort_me
