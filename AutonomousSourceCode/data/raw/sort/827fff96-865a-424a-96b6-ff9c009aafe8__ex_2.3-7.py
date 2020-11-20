def merge(a, p, r, q):
	sorted_a = []

	i = p
	j = r+1

	while i <= r and j <= q:
		if a[i] < a[j]:
			sorted_a.append(a[i])
			i += 1
		else:
			sorted_a.append(a[j])
			j += 1

	if i <= r:
		sorted_a.extend(a[i:r+1])
	elif j <= q:
		sorted_a.extend(a[j:q+1])

	a[p:q+1] = sorted_a

def merge_sort(a, p, q):
	if p != q:
		r = (p+q) // 2
		merge_sort(a, p, r)
		merge_sort(a, r+1, q)
		merge(a, p, r, q)

def binary_search(a, v, start, end):
	while start <= end:
		m = (start+end) // 2
		if a[m] == v:
			return m
		elif a[m] > v:
			end = m-1
		else:
			start = m+1

	return -1

def has_summands(a, x):
	merge_sort(a, 0, len(a)-1)
	for i in range(len(a)-1):
		s1 = a[i]
		s2 = x - s1
		if binary_search(a, s2, i+1, len(a)-1) > -1:
			return s1, s2

	return None

a = [7, 1, 2, 3, 0, 1]
for i in [0, 9, 5, 3, 2]:
	print "%d = %s" % (i, has_summands(a, i))
