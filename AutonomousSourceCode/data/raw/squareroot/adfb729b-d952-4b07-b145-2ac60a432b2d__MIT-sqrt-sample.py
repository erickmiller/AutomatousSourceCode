def squareRootBi(x, epsilon):
	"""assume x>=0 and epsilon >0
	Return y if abs(y**2-x) < epsilon"""
	assert x>=0, "must be non-negative, not" +str(x)
	assert epsilon>0, "must be positive, not" +str(epsilon)
	low=0
	high=max(x, 1.0)
	guess=(low+high)/2.0
	ctr=1
	while abs(guess**2-x)>epsilon and ctr<=100:
		# print "low:", low, "high:", high, "guess:", guess
		if guess**2<x:
			low=guess
		else:
			high=guess
		guess=(low+high)/2.0
		ctr+=1
	assert ctr<=100, "count exceeded"
	print  "calculation cycle", ctr, "candidate", guess
	return guess



# x=float(raw_input("Enter x: "))
# epsilon=float(raw_input("Enter epsilon: "))
# squareRootBi(x, epsilon)

def squareRootNR(x, epsilon):
	ctr=0
	assert x>=0, "must be non-negative, not " +str(x)
	assert epsilon>0, "must be a positive, not "+str(epsilon)
	ans=x/2.0
	# ans=.0001
	while abs(ans**2 - x)>epsilon and ctr<=100: 
		ans=ans-(ans**2-x)/(2*ans)
		ctr+=1
	assert ctr<=100, "Iteration count exceeded"
	print "NR method: ctr: ", ctr,  "candidate", ans
	return ans	


def testbi():
	print "squareRootBi(4, 0.0001)"
	squareRootBi(4, 0.0001)
	print "squareRootBi(9, 0.0001)"
	squareRootBi(9, 0.0001)
	print "squareRootBi(2, 0.0001)"
	squareRootBi(2, 0.0001)
	print "squareRootBi(0.25, 0.0001)"
	squareRootBi(0.25, 0.0001)

def compareMethods():
	print "squareRoot (2, .01) "
	squareRootBi(2, .01)
	squareRootNR(2, .01)
	raw_input()
	print "squareRoot (2, .0001) "
	squareRootBi(2, .0001)
	squareRootNR(2, .0001)
	raw_input()
	print "squareRoot (2, .000001) "
	squareRootBi(2, .000001)
	squareRootNR(2, .000001)
	raw_input()


compareMethods()