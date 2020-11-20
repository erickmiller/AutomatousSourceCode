def sort_fractions(fractions):
	arr = sorted(fractions,key = lambda x : x[0]/x[1])
	return arr