import math
import itertools

#Naive method.
def get_largest_prime_factor(number):
    possible_factors = itertools.count(2)
    square_root_num = math.sqrt(number)

    for num in possible_factors:

        if num > square_root_num:
            break

        if num >= number:
            break

        while number / num % 1 == 0:
            if number / num != 1:
                number /= num

    return number

#print(str(int(getLargestPrimeFactor(9007199254740992))))
print(str(int(get_largest_prime_factor(600851475143))))