def sort_last(tuples):
	b = sorted(tuples, key = lambda x:x[-1])
	return b


print sort_last([(1, 3), (1, 7), (2, 2), (3, 4, 5)])



