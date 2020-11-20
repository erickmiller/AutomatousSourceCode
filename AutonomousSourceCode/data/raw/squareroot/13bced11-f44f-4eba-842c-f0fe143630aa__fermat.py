# Samir Silbak
# Cryptography 1

import gmpy2

def is_prime(exponent):
    for k in range(0,10000000):
        p = 10**exponent + k
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            print "k = ", k
            return

def square_roots(base, prime):
        exponent = (prime + 1)/4
        root_1 = (base ** exponent) % prime
        root_2 = prime - root_1

        print "\n"
        print "first root = %i \nsecond root = %i\n" % (root_1, root_2)
        return

def probable_prime(prime, count):
    for k in range(1,10000000):
        p = prime + k
        a = gmpy2.powmod(2, p-1, p)

        if (a == 1): 
            print "k = ", k
            count += 1

            if count == 4: 
                return

is_prime(10)
is_prime(25)
is_prime(50)

square_roots(5739,100003)
probable_prime(16157879263,0)
