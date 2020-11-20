

def triangle(n):
    '''return the nth triangle number'''
    return sum(range(1, n + 1))

def n_divisors(n):
    '''count unique divisors of n'''
    ret = 0
    # only need to go to the square root since factors come in pairs (except square root)
    for x in xrange(1, int(n**0.5)+1):
        if n % x == 0:
            if x**2 != n: # add 2 factors (for x and n/x)
                ret += 2
            else: # unless it's the square root, in case it only counts once
                ret += 1
    return ret

def search():
    # search semi-efficiently until we have enough triangle numbers
    top = 100
    while True:
        print top
        for x in range(top):
            t = triangle(x)
            if n_divisors(t) > 500:
                return t
        top *= 2

print search()



