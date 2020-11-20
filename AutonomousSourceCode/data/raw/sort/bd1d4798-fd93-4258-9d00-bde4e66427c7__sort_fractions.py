from simplify_fraction import simplify_fraction

def evaluate_fraction(fraction):
	return float(fraction[0]) / fraction[1]


def sort_fractions(fractions):
	return(sorted(fractions, key=evaluate_fraction))


#print (sort_fractions([(2, 3), (1, 2), (1, 3)]))
#stoqn e geniiii
