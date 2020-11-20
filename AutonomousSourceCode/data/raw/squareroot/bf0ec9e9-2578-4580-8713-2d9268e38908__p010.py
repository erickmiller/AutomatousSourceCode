
import math

def is_prime(N):
	square_root = math.sqrt(N)
	dividers = [ d for d in range(2,int(square_root)+1) ]
	for d in dividers:
		if N % d == 0:
			return False
	return True

N=2000000
ints = range(2,N+1)
primes = []
for i in ints:
	if is_prime(i):
		primes.append(i)
sum_prime=sum(primes)

f = open('p010.txt','w')
f.write(str(sum_prime))
f.close()