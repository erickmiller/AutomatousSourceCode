import math
def factors(number):
	t = 0	
	square_root = int(math.sqrt(number))
	for i in range(square_root,0,-1):
		if number % i == 0:
			t = t + 1
	if number == pow(square_root,2):
		return (2 * t) - 1
	else:	
		return 2 * t

a,b,factor_count = 1,2,3
while factor_count < 500:
	a,b = a+1,b+1
	if a%2==0:
		factor_count = factors(a/2)*factors(b)-1
	else:
		factor_count = factors(a)*factors(b/2)-1

print "The Number = ",(a*b)/2," and Number of Factors=",factor_count
