import math

def getContinuedFractionOfSquareRoot(val):
	m = [0]
	d = [1]
	a = [int(math.sqrt(val))]
	yield a[0]
	
	while True:
		mm = d[-1]*a[-1] - m[-1]
		dd = (val - mm*mm) / d[-1]
		aa= int( (a[0] + mm)/dd )
		m.append(mm)
		d.append(dd)
		a.append(aa)
		yield aa


def checkPellSolution(x,y,n):
	return x*x - n*y*y == 1


def solve(D):
	if int(math.sqrt(D))**2 == D:
		return
	
	continuedFractionGenerator = getContinuedFractionOfSquareRoot(D)
	a = continuedFractionGenerator.next()
	p = [1, a]
	q = [0, 1]
	
	for a in continuedFractionGenerator:
		if checkPellSolution(p[-1], q[-1], D):
			return (p[-1], q[-1])
			
		p.append(a*p[-1] + p[-2])
		q.append(a*q[-1] + q[-2])


for D in xrange(1,1001):
	result = solve(D)
	if result is None:
		print 'No solution for D= %d' % D
		continue
		
	print 'Solution for D= %d: x= %d, y=%d' % (D, result[0], result[1])
	

