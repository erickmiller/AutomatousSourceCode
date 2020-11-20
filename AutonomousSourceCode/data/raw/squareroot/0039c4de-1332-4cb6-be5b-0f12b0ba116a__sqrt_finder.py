def FindOrderMagnitude(n):
	o = 0

	while (n >= 1):
		n /= 10
		o += 1

	return o

def FindSquareRoot(n, eps):
	assert(n >= 0)

	low = 0.0
	upp = n

	k = 0
	r = (low + upp) * 0.5
	## r = 10 ** (FindOrderMagnitude(n) * 0.5)
	e = abs((r * r) - n)

	## binary-search
	while (e > eps):
		if ((r * r) >= n):
			upp = r
		else:
			low = r

		r = (low + upp) * 0.5
		e = abs((r * r) - n)
		k += 1

	return (r, k)

(r0, k0) = FindSquareRoot(123.456, 0.01)
(r1, k1) = FindSquareRoot(777.777, 0.01)

print("sqrt=%f (%f) iters=%d" % (r0, r0 * r0, k0))
print("sqrt=%f (%f) iters=%d" % (r1, r1 * r1, k1))

