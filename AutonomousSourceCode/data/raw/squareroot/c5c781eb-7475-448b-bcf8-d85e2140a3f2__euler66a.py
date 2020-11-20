def euler66():
	ans, ansmax = 0, 0
	for num in xrange(2, 1001):
		try:
			x, y = getApprox(num)
			if x > ansmax:
				ans, ansmax = num, x
		except StandardError:
			continue
	print ans

def continuedroot(number):
	from math import sqrt
	m, d, a, continued, Done = 0, 1, int(sqrt(number)), [], False
	a0 = a
	if a0**2 == number:
		raise StandardError("Cannot find a continued fraction for the root of a perfect square")
	else:
		while a != 2*a0:
			m = d*a-m
			d = (number - m**2)/d
			a = (a0+m)/d
			continued.append(a)
		return a0, continued

def getApprox(square):
	integer, fract = continuedroot(square)
	idx, cycle = 0, len(fract)
	num, denom  = 1, fract[idx]
	a, b = 1, 1
	while a**2-square*b**2 != 1:
		idx += 1
		a, b = integer*denom+num, denom
		denom, num = denom*fract[idx%cycle] + num, denom
	return a, b

if __name__ == "__main__":
	euler66()
