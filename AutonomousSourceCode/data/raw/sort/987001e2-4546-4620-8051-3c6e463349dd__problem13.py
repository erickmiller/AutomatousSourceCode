""" Write a function lensort to sort a list of strings based on length.
"""

def lensort(lists):
	return sorted(lists, key = lambda x:len(x))
print lensort(['python', 'java', 'c', 'ruby', 'lisp', 'haskall'])
