def anagram_check(strings): 
	q=['orchestra','asian']
	li_sort = sorted(list(strings))
	for word in q:
		z = sorted(list(word))
		if z == li_sort:
			return word
print anagram_check('carthorse')
