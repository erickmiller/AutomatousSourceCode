# Write a  fn called 'is_sorted' that takes a list as a
# parameter and returns TRUE if the list is sorted in ascending order and
# False otherwise !

def is_sorted(t):
	orig = t[:]
	t.sort()
	if t == orig:
		return True
	else:
		return False

t = [5,1,3,9]
print "Initial List : ",
print t

case = is_sorted(t)

if case == True:
	print "Yeah..!! That list is Sorted "
else:
	print "It's not sorted"
