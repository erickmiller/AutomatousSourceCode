from math import sqrt

def get_factors(num):
	count = 0
	root = int(sqrt(num)) + 1

	#run from i to the square root of num.  when we find a match, add by 2
	for i in xrange(1, root):
		if num % i == 0:
			count += 2

	#take 1 away because we counted too many when it's a perfect square
	if root * root == num:
		count -= 1
	return count

def triangular_number(divisors):
	count = 1
	triangle_num = 1
	factors = []

	while get_factors(triangle_num) < divisors:
		count += 1
		triangle_num += count
		factors = get_factors(triangle_num)
		
	return triangle_num

print triangular_number(500)