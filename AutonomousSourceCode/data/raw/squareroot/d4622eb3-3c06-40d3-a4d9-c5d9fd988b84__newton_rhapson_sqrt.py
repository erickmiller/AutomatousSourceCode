##print " this program computes square root of a number using"
##print "newton-rhapson method"
##
##number=float(input("Enter the number whose square root is desired "))
##
##guess_estimate = float(number/2.0)
##
##while (guess_estimate*guess_estimate != number):
##
##    quotient = (number / guess_estimate)
##    new_guess = (quotient+guess_estimate)/2
##    if guess_estimate ==new_guess:
##        print "the square root is", guess_estimate
##        break
##    else:
##        guess_estimate = new_guess
        
import math

def average(a,b):
    return (a+b)/2.0

def improve (guess,x):
    return average(guess, x/guess)

def good_enough(guess,x):
    d = abs(guess*guess-x)
    return (d < 0.000001)

def square_root(x):
    guess = 1
    while (not good_enough(guess,x)):
        guess = improve(guess,x)
    return guess

 


