
# Plus grand diviseur

import math

def is_prime(N):
	square_root = math.sqrt(N)
	dividers = [ d for d in range(2,int(square_root)+1) ]
	for d in dividers:
		if N % d == 0:
			return False
	return True

N = 600851475143

square_root = math.sqrt(N)
int_range = range(1,int(square_root)+1)
int_range.reverse()

for i in int_range:
	if N % i == 0 and is_prime(i):
		break

f = open('p003.txt','w')
f.write(str(i))
f.close()