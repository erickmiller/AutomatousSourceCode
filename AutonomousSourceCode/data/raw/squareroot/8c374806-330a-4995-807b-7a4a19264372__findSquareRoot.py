def findSquareRoot(number):
    low = 0.0
    high = number
    epsilon = 0.00000000001
    guess = (low + high) / 2
    
    while abs(number - guess**2) >epsilon:
        print "high:  " + str(high) + "  low:  " + str(low) + "  guess:   " +str(guess)
        if guess**2 < number:
            low = guess
        elif guess**2 > number:
            high = guess
        elif guess**2 == number:
            return "found square root of" + str(number) + 'would be' + str(guess)
        guess = (low + high)/2
    return "Approximate square root " + str(number) + ' is ' + str(guess)
    