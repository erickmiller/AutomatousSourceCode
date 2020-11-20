import math

def is_prime(n):
	if n < 2:
		return False
	i = 2
	while (i*i) <= n:
		if n%i == 0:
			return False
		i+=1
	return True

def is_palindromic(num):
    return str(num) == str(num)[::-1]

def square_sum(num):
	root = int(math.sqrt(num))
	sum = 0
	index = 1
	while index < root:
		sum = 0
		for i in xrange(index, root+1):
			sum += i*i
			if sum == num:
				print i,sum
				return True
			if sum > num:
				break
	
		index+=1
	return False

numbers = []
for i in xrange(1,100000000):
	if is_palindromic(i) and square_sum(i):
		numbers.append(i)

print sum(numbers)