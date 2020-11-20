import collections

def sort_fractions(fractions):
	numbers = {}
	result = []

	for fraction in fractions:
		numbers[fraction] = fraction[0] / fraction[1]
	result = sorted(numbers, key=lambda key: numbers[key])
	return result

