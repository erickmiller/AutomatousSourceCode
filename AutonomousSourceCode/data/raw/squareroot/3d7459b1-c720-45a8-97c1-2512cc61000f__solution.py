from math import sqrt


def is_prime(potential_prime, primes_so_far):
    square_root_of_prime = sqrt(potential_prime)

    for prime in primes_so_far:
        if prime > square_root_of_prime:
            return True
        if potential_prime % prime == 0:
            return False

    return True


def generate_primes_up_to(n):
    primes_so_far = [2]

    for potential_prime in range(3, n + 1, 2):
        if is_prime(potential_prime, primes_so_far):
            primes_so_far.append(potential_prime)

    return primes_so_far

if __name__ == '__main__':
    print(sum(generate_primes_up_to(2000000)))
