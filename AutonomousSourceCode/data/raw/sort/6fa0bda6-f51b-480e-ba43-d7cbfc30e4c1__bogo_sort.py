from random import shuffle

def is_sorted(list):
	for e in range(0, len(list)-1):
		if list[e] > list[e+1]:
			return False
	return True

def bogo_sort(sort_me):
	'''
	bogo_sort(list) uses bogo sort algorithm to sort a list.
	It accepts a list and returns a sorted list.

	>>> my_list = bogo_sort(my_list)
	'''
	while not is_sorted(sort_me):
		shuffle(sort_me)
	return sort_me
