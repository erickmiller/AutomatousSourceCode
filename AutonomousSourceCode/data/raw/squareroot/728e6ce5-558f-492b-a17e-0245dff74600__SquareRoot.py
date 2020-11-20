def findSquareRoot(number):
    low= 0.0
    high = number
    epsilon =0.01
    guess = (low + high) / 2 
    
    while abs((number) - guess**2) >epsilon:
        if guess**2 < number:
            low = guess 
        elif guess**2 > number:
            high = guess 
        elif guess**2 == number:
            return "The square root of" + str(number) + "would be" +str(guess) 
        guess = (low + high)/2
    return "The aproximate square root of " + str(number) + " is " + str(guess)
        