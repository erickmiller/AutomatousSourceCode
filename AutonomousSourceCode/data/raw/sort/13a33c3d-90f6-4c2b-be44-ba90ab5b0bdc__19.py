def is_increasing(seq):

	sort = sorted(seq)
	if seq == sort:
		return True
	else:
		return False

print is_increasing([1,2,3,4,5])
print is_increasing([5,6,-10])
