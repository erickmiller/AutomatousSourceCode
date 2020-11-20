

def root(x):
    epsilon = 0.01
    guess = x/2.0
    while abs(guess*guess - x) >= epsilon:
        guess = guess - (((guess**2) - x)/(2*guess))
        
    return guess
    #print('Square root of ' + str(x) + ' is about '+ str(guess))
    
def square(x):
    return x**2
  
z = square(3)  
print z