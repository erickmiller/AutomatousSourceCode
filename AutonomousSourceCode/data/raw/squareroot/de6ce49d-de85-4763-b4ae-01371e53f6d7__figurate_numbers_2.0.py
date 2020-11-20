import math

limit = 1000

primes = [2]
triangular = []
tetrahedrals = []


#find prime
index = 3

while index <= limit:

    remainders = []
    j = 0

    while j < len(primes):
        remainders.append(index % primes[j])

        j = j + 1

    if 0 not in remainders:
        primes.append(index)

    index = index + 1
        
#find triangular
index = 1
while index <= limit:
    if (math.sqrt(index * 8 + 1) - 1) % 2 == 0:
        triangular.append(index)
    index += 1

#def find_tetrahedrals(limit):

j = 1
while j <= len(triangular):
    
    tetrahedrals.append(sum(triangular[:j]))
    j = j + 1
        
def is_prime(n):

    return n in primes


def is_triangular(n):
    """To tell whether n is a triangular number"""
    return n in triangular
#the summation formula of arithmetic sequence is sum = (m + 1) * m / 2

def is_tetrahedral(n):
    """To tell whether n is a tetrahedral number"""
    return n in tetrahedrals

def is_square(n):

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
#If remainder == 0, then n is ansquare piramidal number.

def is_pentagonal(n):
    """To tell whether n is a pentagonal number"""
    return (math.sqrt(n * 24 + 1) + 1) % 6 == 0
#the general ofrmula of pentagonal sequence is n = (3 * m - 1) * m / 2

def is_prime_oblong(n):

    prime_oblong = False
    j = 0

    while j < len(primes):

        if n % primes[j] == 0 and n / primes[j] in primes:
            prime_oblong = True
            break
        j = j + 1

    return prime_oblong

def is_pointy(n):

    pointy = False

    j = 0
    while j < len(tetrahedrals):
        if n - tetrahedrals[j] in tetrahedrals and n != 2 * tetrahedrals[j]:
            pointy = True
            break
        j += 1
    
    return pointy
    
def print_result(n):
    
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

    i = 1
    while i <= limit:
        print_result(i)
        i += 1
    
if __name__ == "__main__":
    main()
