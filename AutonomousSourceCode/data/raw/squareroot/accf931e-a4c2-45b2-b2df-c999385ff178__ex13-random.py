# the following program let the user play a game where he has to guess the square of
# a random number
# modify it as follow:
# print the square of an natural number and let the player guess the square root.
# the square root should be between 1 and 20

import random

def askForNumber():
    return int(raw_input("Enter square of x: "))

x = random.randint(1,10)

print "x =",x

inputValue = askForNumber()  
while inputValue!=x*x:
    print "Answer is wrong!"
    inputValue = askForNumber()

print "Right!"    
    
    




