# Chapter 7
# Section 7.2

def countdown(n):
    while n > 0:
        print n
        n = n - 1
    print 'Blastoff!'

countdown(10)

def sequence(n):
    while n != 1:
        print n,
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1

sequence(80)
sequence(45)
sequence(20.7)
sequence(35.7985654)

# Ex. 7.1
def print_n(s,n):
    while n >= 0:
        print s
        n = n - 1

print_n('Hello',5)

# Section 7.5 Square roots
# Ex. 7.2
def approx_sqrt(a,g):
    """ Returns the aproximation of the square root of the first parameter accurate to ten decimal places. The second parameter is your guess of what the square root is.
    """
    import math
    if g < 0:
        print 'The square root of a number is never negative. Guess a positive value'
        return
    while True:
        m = (g+(a/(g*1.0)))/2.0
        if math.fabs(g-m) < (10**(-10)):
            return m
        g = m

print approx_sqrt(38,6)

# Ex. 7.4
def eval_loop():
    while True:
        r = raw_input('Mathematical expression = ')
        if r == 'done' or r == 'Done':
            break
        print eval(r)
    print 'Done!'
    return

eval_loop()
