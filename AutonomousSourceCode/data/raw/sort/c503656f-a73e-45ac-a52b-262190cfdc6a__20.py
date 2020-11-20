def is_decreasing(seq):

	sort = sorted(seq)
	reverse = sorted(sort, reverse=True)
	if reverse == seq:
		return True
	else:
		return False
	
print is_decreasing([5,4,3,2,1])
print is_decreasing([1,2,3])
