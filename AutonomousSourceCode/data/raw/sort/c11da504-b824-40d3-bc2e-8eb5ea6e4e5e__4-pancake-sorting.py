import numpy as np

def flip(a,i,j):
	temp = a[i:j+1]
	temp = temp[::-1]
	a[i:j+1] = temp
	return a

def pancake_sort(a):
	sorted_ind = -1
	while sorted_ind != len(a) - 1:
		max_unsorted = sorted_ind+1
		for i in xrange(sorted_ind+2,len(a)):
			if a[i] >= a[max_unsorted]:
				max_unsorted = i
		if max_unsorted < len(a) - 1:
			a = flip(a, max_unsorted, len(a))
		elif max_unsorted == len(a)-1:
			a = flip(a, sorted_ind+1, len(a)-1)
			sorted_ind += 1
	return a

print pancake_sort(np.random.randint(100, size=10))
