import math
from helpers import helpers

MAX_RANGE = 10000

def is_square(num):
    root = math.sqrt(num)
    return root == int(root)

def get_smallest_not_satisfying_golbach():
    primes = []

    for candidate in range(3, MAX_RANGE, 2):
        # If it is a prime
        if helpers.is_prime(candidate):
            # Store it in the primes list
            primes.append(candidate)
        else:
            # If it cannot be written as the sum of a prime and a square
            if not any(is_square((candidate - prime) / 2) for prime in primes):
                return candidate

def main():
    answer = get_smallest_not_satisfying_golbach()
    print(answer)

if __name__ == '__main__':
    main()
