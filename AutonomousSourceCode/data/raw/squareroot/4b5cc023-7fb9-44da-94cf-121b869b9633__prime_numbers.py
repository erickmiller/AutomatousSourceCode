import math

@profile
def is_prime_slower(num):
    if num <= 1:
        return False
    
    square_root = int(math.sqrt(num))
    for i in range(2,square_root + 1):
        if num % i == 0:
            return False
    return True

@profile
def is_prime(num):
	if num == 1:
		return False

	if num < 4: # 2 and 3 are prime
		return True

	if num % 2 == 0:
		return False

	if num < 9: # We have already excluded 4,6 and 8.
		return True

	if num % 3 == 0:
		return False

	r = int(math.sqrt(num))
	f = 5

	while f <= r:
		if num % f == 0:
			return False
		if num % (f+2) == 0:
			return False
		f += 6

	return True

def main():
	for i in range(0,1000000000):
		is_prime(i)
		is_prime_slower(i)
	

if __name__ == '__main__':
	main()