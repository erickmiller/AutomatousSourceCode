import math

def M(n, count):
	# a > b > c
	for s in range(1, 2 * n + 1):
		if is_square(n, s):
			b_max = min(n, s - 1)
			b_min = max(1, (s + 1)//2) 
			count += 1 + b_max - b_min
	return count

def is_square(a, b):
	s = a * a + b * b
	root = math.sqrt(s)
	return root == int(root)

i = 1
count = 0
# print(M(100, 0))
while True:
	i += 1
	count = M(i, count)
	if (count > 1000000):
		print(i, count)
		break

# print(M(1000))