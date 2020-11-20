def quick_sort(sort_me):
	'''
	quick_sort(list) uses quick sort algorithm to sort a list.
	It accepts a list and returns a sorted list.

	>>> my_list = quick_sort(my_list)
	'''
	if len(sort_me) < 2:
		return sort_me
	pivot = sort_me[ randint(0, len(sort_me)-1) ]
	smaller = quick_sort([x for x in sort_me if x < pivot])
	this = [x for x in sort_me if x == pivot]
	bigger = quick_sort([x for x in sort_me if x > pivot])
	return smaller + this + bigger
