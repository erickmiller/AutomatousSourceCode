#a function lensort to sort a list of strings based on length.
def lensort(lists):
	return sorted(lists,key=lambda x:len(x))
lists=['fgdf','dfg','yuyju']
print lensort(lists)
