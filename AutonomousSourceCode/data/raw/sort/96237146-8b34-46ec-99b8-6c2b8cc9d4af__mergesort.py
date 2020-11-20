
def merge(a, b):
	"""Merging subroutine. Meant to merge two sorted lists into a combined, sorted list."""
	n = len(a) + len(b)
	d = [0 for i in range(n)]
	i = 0
	j = 0
	for k in range(n):
		if a[i] < b[j]:
			d[k] = a[i]
			if i+1 > len(a)-1:
				for l in b[j:]:
					d[k+1] = b[j]
					k += 1
					j += 1
				return d
			i += 1
		elif a[i] > b[j]:
			d[k] = b[j]
			if j+1 > len(b)-1:
				for l in a[i:]:
					d[k+1] = a[i]
					k+=1
					i+=1 
				return d
			j += 1

def merge_sort(c):
	"""Recursive merge sort. Takes non-repeating list and returns sorted version of the list."""
	if len(c) == 1:
		return c
	else:
		a = merge_sort(c[:int(len(c)/2)])
		b = merge_sort(c[int(len(c)/2):])
		return merge(a,b)

