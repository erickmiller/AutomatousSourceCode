
import math

def squareRootBisect (num, precise = 3):
    ''' Returns closest square-root of a number,
        using Bisection search algorithm.
        @num : The number for which square root is needed
        @precise: Precise upto number precise number of digits
    '''
    if num < 0:
        return -1
    elif num == 0:
        return 0
    step = 0.1
    precission = step / ((10**precise))
    start = 0
    end = num
    while ( True ):
        mid = (start + end) / 2.0
        squareTillNow = mid*mid
        if abs(squareTillNow - num) < precission:
            break
        else:
            if squareTillNow > num:
                end = mid
            else :
                start = mid
        print "Mid : ", mid
    return mid
     

def squareRootNR (num, precise = 3):
    ''' Returns closest square-root of a number,
        using Newton-Rapson approximation algorithm.
        @num : The number for which square root is needed
        @precise: Precise upto number precise number of digits
    '''
    if num < 0:
        return -1
    elif num == 0:
        return 0
    step = 0.1
    precission = step / ((10**precise))
    guess = num / 2.0
    while (True):
        squareTillNow = guess * guess
        if abs(squareTillNow - num) < precission:
            break
        else :
            guess = guess - ((squareTillNow - num) / (2*guess))
            ''' x(n+1) = f( x(n) ) - ( f( x(n) ) / f'( x(n) ) ) 
                Where f(x (n)) is (x(n) - num )^2 
                f (x) is approximate squared error 
            '''
        print "Guess : ", guess
    return guess


print squareRootBisect (10001, 4)
print squareRootNR (10001, 6)
