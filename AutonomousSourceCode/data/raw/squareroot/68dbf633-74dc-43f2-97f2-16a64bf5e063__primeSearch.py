from sys import argv
from math import sqrt

def prime_search(maximum):
		primes = [2, 3]
		for num in range(5,maximum,2):
			squareRoot = sqrt(num)
			for prime in primes:
				if num % prime == 0:
					break
				elif prime > squareRoot:
					primes.append(num)
					break
		return primes

def save_primes(primeNumbers ,pathName = "prime.txt"):
		with open(pathName,'w') as f:
			for number in primeNumbers:
				f.write(str(number) + "\n")
def main():
		argue = len(argv)

		if argue <= 1 or argue > 3:
			print("Usage: primeSearch.py Length_of_Search <filename>")
			quit()
		elif argue == 2:
			primeFound = prime_search(int(argv[1]))
			save_primes(primeFound)
		elif argue == 3:
			primeFound = [prime_search(int(argv[1]))]
			save_primes(primeFound, argv[3])

if __name__ == '__main__':
	main()