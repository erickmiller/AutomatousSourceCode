"""
bubble_sort.py

Worse Case Performance: O(n^2)
Best Case Performance: O(n)
Average Case Performance: O(n^2)

Pseudocode: http://en.wikipedia.org/wiki/Bubble_sort#Pseudocode_implementation
"""


def bubble_sort(sequence):
	sorted = False
	
	while not sorted:
		sorted = True
		for i in range(0,len(sequence)-1):
			if sequence[i] > sequence[i+1]: #found unsorted
				sorted = False
				tmp = sequence[i+1]
				sequence[i+1] = sequence[i]
				sequence[i] = tmp
	
	return sequence


