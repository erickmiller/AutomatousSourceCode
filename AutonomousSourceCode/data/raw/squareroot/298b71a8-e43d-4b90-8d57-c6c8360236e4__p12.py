import math

def is_prime(num):
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def prime_factor_powers(num):
    square_root = int(math.sqrt(num)) + 1
    prime_factors = []
    
    for i in range(2,square_root):
        if num % i == 0:
            if is_prime(i):
                prime_factors.append(i)

    prime_factor_powers = []

    # calculating powers of factors
    for prime_factor in prime_factors:
        dividend = num
        power = 0
        while dividend % prime_factor == 0:
            dividend /= prime_factor
            power += 1
        prime_factor_powers.append(power)

    return prime_factor_powers

def solution():
    n = 1
    triangle_number = 1
    num_divisors = 1
    prime_powers = []

    while num_divisors <= 500:
        n += 1
        triangle_number += n
        prime_powers = prime_factor_powers(triangle_number)
        product = 1
        for power in prime_powers:
            product *= power + 1
        num_divisors = product 

    return n, triangle_number, num_divisors

solution()