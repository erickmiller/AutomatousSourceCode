#!/usr/bin/python

import sys

def insertionSort(a, verbose):
	sortedStart = len(a) - 1
	while sortedStart > 0:
		print "sortedStart =", sortedStart
		for i in xrange(sortedStart - 1, len(a)):
			if i < len(a) - 1 and a[i] > a[i + 1]:
				print "// swapping %s with %s" % (a[i], a[i + 1])
				temp = a[i]
				a[i] = a[i + 1]
				a[i + 1] = temp
				if verbose:
					print a
		sortedStart -= 1
	return a

verbose = sys.argv[1].lower() == "true"
sortThis = [ int(x) for x in sys.argv[2:] ]
print "Unsorted ->\t", sortThis
sortedThis = insertionSort(sortThis, verbose)
print "Sorted ->\t", sortedThis
