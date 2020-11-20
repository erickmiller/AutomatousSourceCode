##Authors: Dichen Li and Anders Schneider
##September 8, 2014

import math

def is_prime(n):
    """This determines if n is prime by dividing n by all numbers smaller than the square root of n"""
    i = 2
    prime = True

    if n == 1:
        prime = False

    while i <= int(n ** 0.5):
        if n % i == 0:
            prime = False
            break
        i = i + 1

    return prime

def is_triangular(n):
    """To tell whether n is a triangular number"""
    return (math.sqrt(n * 8 + 1) - 1) % 2 == 0
#the summation formula of arithmetic sequence is sum = (m + 1) * m / 2

def is_tetrahedral(n):
    """To tell whether n is a tetrahedral number"""
    m = 0
    f_m = 0
    tetrahedral = False
    while n - f_m > 0:
        m += 1
        f_m = (m ** 3 + 3 * m * m + 2 * m) / 6
        if f_m - n == 0:
            tetrahedral = True
            break
    return tetrahedral
#the general formula of tetrahedral sequence is n = f(m) = (m^3 + 3 * m^2 + 2 * m) / 6

def is_square(n):
    """Determines if n is square by taking the square root and evaluating if the result is an integer"""
    return n ** 0.5 % 1 == 0

def is_square_pyramidal(n):
    """To tell whether n is a tetrahedral number"""
    remainder = n
    subtractor_root = 0
    while remainder > 0:
        subtractor_root += 1
        remainder -= subtractor_root ** 2
    return remainder == 0
#n is subtracted by 1^2, 2^2, ... subtractor_root^2 until it is equal to or smaller than 0 (remainder <=0).
#If remainder == 0, then n is a square pyramidal number.

def is_pentagonal(n):
    """To tell whether n is a pentagonal number"""
    return (math.sqrt(n * 24 + 1) + 1) % 6 == 0
#the general formula of pentagonal sequence is n = (3 * m - 1) * m / 2

def is_prime_oblong(n):
    """Determines if n is prime oblong by dividing by every number smaller
    than n and evaluating if that number and n are prime and distinct"""
    i = 2
    prime_oblong = False

    while i <= int(n ** 0.5):

        if n % i == 0 and is_prime(i) and is_prime(n/i) and n/i != i:
            prime_oblong = True

        i = i + 1

    return prime_oblong

def is_pointy(n):
    """To tell whether n is a pointy number"""
    i = 1
    pointy = False
    while i < n / 2:
        if is_tetrahedral(i) and is_tetrahedral(n - i):
            pointy = True
            break
        i += 1
    return pointy
#From i = 1 to n / 2, test whether i and n - i are both tetrahedrals.

def print_result(n):
    """This function generates a string depending on if n is prime, square, etc."""
    
    str_prime = 'composite'
    str_triangular = 'not triangular'
    str_tetrahedral = 'not tetrahedral'
    str_square = 'not square'
    str_square_pyramidal = 'not square pyramidal'
    str_pentagonal = 'not pentagonal'
    str_prime_oblong = 'not prime oblong'
    str_pointy = 'not pointy'
    
    if is_prime(n):
        str_prime = 'prime'
    if is_triangular(n):
        str_triangular = 'triangular'
    if is_tetrahedral(n):
        str_tetrahedral = 'tetrahedral'
    if is_square(n):
        str_square = 'square'
    if is_square_pyramidal(n):
        str_square_pyramidal = 'square pyramidal'
    if is_pentagonal(n):
        str_pentagonal = 'pentagonal'
    if is_prime_oblong(n):
        str_prime_oblong = 'prime oblong'
    if is_pointy(n):
        str_pointy = 'pointy'
    print '%d %s, %s, %s, %s, %s, %s, %s, %s' % (n, str_prime, str_triangular, str_tetrahedral, str_square, str_square_pyramidal, str_pentagonal, str_prime_oblong, str_pointy)

def main():
    """From 1 to upper limit, this function executes the print function"""
    limit = 1000
    
    i = 1
    while i <= limit:
        print_result(i)
        i += 1
    
if __name__ == "__main__":
    main()
