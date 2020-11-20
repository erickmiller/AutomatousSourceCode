import math

def eratosthenesSeive(limit):
	limit = limit+1
	notPrime = set()
	primes = []
	for i in range(2, limit):
		if i in notPrime:
			continue
		for f in range(i*2, limit, i):
			notPrime.add(f)
		primes.append(i)
	return primes

def checkSquare(n):
	root = int(math.pow(n, .5))
	if root*root == n:
		return True
	return False

primes = eratosthenesSeive(10000)
setOfPrimes = set()
for prime in primes:
	setOfPrimes.add(prime)

def main():
	found = False
	num = 1
	while not found:
		num += 2
		if num not in setOfPrimes:
			i = 0
			foundPrime = False
			while primes[i] < num:
				diff = num - primes[i]
				if checkSquare(diff/2):
					foundPrime = True
					break
				i += 1
			if not foundPrime:
				found = True
	print num

if __name__ == '__main__':
	main()
