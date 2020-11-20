def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a


def int_root(n):
	a = 2**(n.bit_length()/2)
	b = 1
	while True:
		ea,eb =a**2 - n*b**2,2*a*b
		a,b = 2*a**2 -ea,eb
		if abs(ea) < abs(eb):
			x = a/b
			return x,x**2==n

def is_perfect_square(n):
	x = int_root(n)
	return x**2 == n


output = []
for m in range(2,10**5):
	x,sp= int_root(16*m**2 - 4*(m**2 -1))
	if sp:
		n = (4*m - x)/2
		output.append((4*m*n, m**2+ n**2))

	x,sp= int_root(12*(m**2-1))
	if sp:
		n = x/6
		output.append((2*(m**2 - n**2), m**2+ n**2))

total = 0
for x in output:
	total += 2*x[1] + x[0]
	if 2*x[1] + x[0] > 10**9:
		break
	print x,total