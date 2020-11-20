import math
'''
I wrote my own square root function because I thought Decimal.sqrt() was not precise....
it turns out it was just a logic problem, but i'm keeping the function!
'''
def square_root(n, digits):
	limit = math.pow(10, digits+1) 
	a = 5*n
	b = 5
	while b < limit+1:
		if a >= b:
			a -= b
			b += 10
		else:
			a *= 100
			b = (b/10) * 100 + 5
	return b/100


sum = 0
for x in range(2, 101):
	if not math.sqrt(x).is_integer():
		digits = square_root(x, 100)
		if digits > 10:
			while digits >= 1:
				digit = digits % 10
				sum += digit
				digits /= 10

print(sum)
		
