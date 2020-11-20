#square root function

#import sqrt function of math module
from math import sqrt

#function definition
def sqroot(x):
    return sqrt(x)

x = input("Enter number x: ")                   #get user input
print "Square root of x: " + str(sqroot(x))     #output
