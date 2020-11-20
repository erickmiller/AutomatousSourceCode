import urllib
def anagram_check(strings): 
	files = urllib.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt')
	li_sort = sorted(list(strings))
	for word in files:
		z = sorted(list(word.rstrip()))
		if z == li_sort:
			return word.rstrip()
print anagram_check('carthorse')
