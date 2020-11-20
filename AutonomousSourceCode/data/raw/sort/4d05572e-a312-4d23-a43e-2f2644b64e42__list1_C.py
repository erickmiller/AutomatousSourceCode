print "Enter a non empty tuples"

list=input()

def sort_last(s):
	return s[-1]

print sorted(list,key=sort_last)

	
