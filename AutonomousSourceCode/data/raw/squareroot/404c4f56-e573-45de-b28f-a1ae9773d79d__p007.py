
import math

def is_prime(N):
	square_root = math.sqrt(N)
	dividers = [ d for d in range(2,int(square_root)+1) ]
	for d in dividers:
		if N % d == 0:
			return False
	return True

counter = 10001
N = 2
while True:
	if is_prime(N):
		counter -= 1
	if counter == 0:
		break
	N +=1

f = open('p007.txt','w')
f.write(str(N))
f.close()