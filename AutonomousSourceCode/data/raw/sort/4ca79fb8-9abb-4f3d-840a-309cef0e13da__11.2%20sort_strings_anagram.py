# Write a method to sort an array of strings so that all the anagrams are next to each
# other.

def compareStrings(s1, s2):
	if sorted(s1) == sorted(s2):
		return 1
	elif sorted(s1) < sorted(s2):
		return 0
	else:
		return -1

stringArray = ['avc', 'vac', 'ac', 'ad', 'aac', 'caa']

print sorted(stringArray, cmp=compareStrings)