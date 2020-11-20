#!/usr/bin/python
#
# Selection Sort
#


def selection_sort(arr):

	unsorted_sz = len(arr)
	i = 0

	# Loop over every array element finding the next smallest value
	while i < unsorted_sz:

		lowest = i
		j = i + 1

		while j < unsorted_sz:
			if arr[j] < arr[lowest]:
				lowest = j
			j = j + 1

		# swap current and lowest found values
		tmp = arr[lowest]
		arr[lowest] = arr[i]
		arr[i] = tmp

		i = i + 1
	return


t1 = range(1, 11)
t1.reverse()
t1_sorted = t1[:] # shallow copy
t1_sorted.sort()
selection_sort(t1)
if t1 == t1_sorted:
	print "success"
else:
	print "sort failed"


t2 = range(1, 1001)
t2.reverse()
t2_sorted = t2[:] # shallow copy
t2_sorted.sort()
selection_sort(t2)
if t2 == t2_sorted:
	print "success"
else:
	print "sort failed"



