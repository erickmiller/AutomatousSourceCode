from itertools import count

def sortView(n):
	""" Returns character-sorted string representation of input value """
	return ''.join(sorted(list(str(n))))

for n in count(1):
	if sortView(n) == sortView(2*n) == sortView(3*n) == sortView(4*n) == sortView(5*n) == sortView(6*n):
		break

print "Solution found at n = %d " % n
# Solution found at n = 142857 
# [Finished in 0.7s]