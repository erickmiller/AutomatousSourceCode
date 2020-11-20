# Executes merge sort on an unsorted list
# Args:
# 	items: Unsorted list of numbers
#
# Returns:
# 	Sorted list of items
def merge_sort(unsorted_list):

	# If unsorted_list is length = 1, then it's implicitly
	# sorted.  Just return it.   Base case.
	if len(unsorted_list) == 1:
		return unsorted_list


	# Create two new lists
	unsorted_list_a = unsorted_list[0:(len(unsorted_list)/2)]
	unsorted_list_b = unsorted_list[(len(unsorted_list)/2):len(unsorted_list)]

	# Sort them
	sorted_list_a = merge_sort(unsorted_list_a)
	sorted_list_b = merge_sort(unsorted_list_b)

	# Merge the two sorted lists and return
	sorted_list = merge(sorted_list_a, sorted_list_b)

	return sorted_list


# Merges two sorted lists

# Returns:
# 	Sorted list
def merge(list_a, list_b):
	
	sorted_list = []

	# Iterates over the two lists, removing elements and putting
	# them in sorted_list until one of the lists is empty
	while (len(list_a) > 0 and len(list_b) > 0):
		if list_a[0] < list_b[0]:
			sorted_list.append(list_a[0])
			list_a.pop(0)
		else:
			sorted_list.append(list_b[0])
			list_b.pop(0)

	# One of the lists was empty so just add the rest
	# of the non-empty one to sorted_list
	if len(list_a) == 0:
		sorted_list.extend(list_b)
	if len(list_b) == 0:
		sorted_list.extend(list_a)


	return sorted_list



def merge_unit_test():
	list_a = [1,2,8,9]
	list_b = [3,4,6,10,11]
	sorted_list = merge(list_a, list_b)
	print(sorted_list)

	# TODO: Add some assertions here



def merge_sort_test():
	list_a = [3,6,1,3,7,8,0,10,22,323,1,5,4,2,85,39]
	sorted_list = merge_sort(list_a)
	print(sorted_list)
