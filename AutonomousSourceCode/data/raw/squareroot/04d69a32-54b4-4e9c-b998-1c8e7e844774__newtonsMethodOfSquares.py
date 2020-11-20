def newtonSqrt(n):
	approx = 0.5 * n
	better = 0.5 * (approx + n/approx)
	while better != approx:
		approx = better
		better = 0.5 * (approx + n/approx)
	return approx

x = float(input("what number would you like to square root?"))
print (newtonSqrt(x))