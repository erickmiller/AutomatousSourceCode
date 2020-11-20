def iterSqRt(number):
    for counter in range(1,number):
        if counter**2 == number:
            return "square root of" + str(number) + 'is' + str(number)
    return "Failed! Square root of" + str(number) + 'is not' + str(number)
    

def findsquareroot(number):
    low = 0.0
    high = number
    epsilon = 0.001
    guess = (low + high)/ 2
    
    while abs(guess**2 - number) > epsilon:
        print "guess:  " + str(guess**2)
        if guess**2 > number:
            high = guess
        elif guess**2 < number:
            low = guess
        elif guess**2 == number:
            return 'Found square root of' + str(number) 
        guess = (low + high) / 2 
    return 'Found approximate square root of ' + str(number)  + ":    " + str(guess) 