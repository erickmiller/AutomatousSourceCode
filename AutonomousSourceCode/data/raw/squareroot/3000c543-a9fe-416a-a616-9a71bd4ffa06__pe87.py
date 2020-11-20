from sympy import ntheory
import math

def count_prime_power_triples(threshold):
    primes = [p for p in ntheory.primerange(1, math.sqrt(threshold))]
    numbers = set()
    for fourth_root in primes:
        n4 = fourth_root ** 4
        if n4 >= threshold:
            break
        for cube_root in primes:
            n3 = cube_root ** 3
            if n4 + n3 >= threshold:
                break
            for square_root in primes:
                n2 = square_root ** 2
                s = n4 + n3 + n2
                if s >= threshold:
                    break
                # print "%d^2 + %d^3 + %d^4 = %d" % (square_root, cube_root, fourth_root, s)
                numbers.add(s)
    return len(numbers)

print count_prime_power_triples(50)
print count_prime_power_triples(50000000)

