from math import sqrt


def is_prime(n):
    square_root_of_potential_prime = sqrt(n)

    for i in range(2, int(square_root_of_potential_prime) + 1):
        if n % i == 0:
            return False

    return True


def generate_nth_prime(n):
    prime_count = 0
    current_number = 1

    while prime_count < n:
        current_number += 1

        if is_prime(current_number):
            prime_count += 1

    return current_number

if __name__ == '__main__':
    print('10,001st prime number: ', generate_nth_prime(10001))
