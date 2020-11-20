#a function extsort to sort a list of files based on extension.
def extsort(a):
	for i in a:
		return sorted(a,key=lambda x:x[i.find('.'):])
a=['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
print extsort(a)
