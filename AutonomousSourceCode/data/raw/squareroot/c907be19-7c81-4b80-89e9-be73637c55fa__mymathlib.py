def sqrt(n, p):
    #square root arbitrary precision using newton's method
    #http://en.wikipedia.org/wiki/Newton%27s_method#Square_root_of_a_number
    x = 10 #initial guess
    i = 0
    while i < p:
        #x = x - (x*x - n)/(2*x)
        x = (x + n/x)/2
        print x
        i += 1
    
def divisor_count(n):
    """Count number of divisors. Used on problem 12, 179.
    """
    divcount = 0
    tmax = n**0.5
    for t in xrange(1, int(tmax+1)):
        if n % t == 0:
            divcount += 2
    if t == tmax:
        divcount -= 1
    return divcount
        
if __name__ == "__main__":
    sqrt(1919191919,20)