def group_by_anagrams(words):
	words.sort(key=lambda x: sorted(x))
	return words