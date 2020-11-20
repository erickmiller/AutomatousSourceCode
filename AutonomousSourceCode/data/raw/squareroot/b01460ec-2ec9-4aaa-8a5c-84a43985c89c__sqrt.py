# File:    sqrt.py
# Date:    12/6/12
# Author:  Carl Stevenson
# Purpose: To calculate square roots using Newton's method

import math

def main():
    intro()
    number, diff = getInputs()
    calc, actDiff, tries = calcSqrt(number, diff)
    printResults(number, diff, calc, actDiff, tries)

def intro():
    print("This program will calculate the square root")
    print("of a number using Newton's Method.")
    print("You will enter the number and the size of the")
    print("difference between Newton's Method square root")
    print("and the real square root.")
    print("Written by Carl Stevenson")
    print()

def getInputs():
    number = eval(input("Enter the number to find its square root: "))
    print()  # for turnin
    # to prevent code wrap
    string="Enter the difference between the calculate and real square root: "
    diff = eval(input(string))
    print()  # for turnin
    return number, diff

def calcSqrt(number, diff):
    newguess = number / 2.0
    tries = 0
    oldguess = 1
    calc = 0
    while abs((newguess - oldguess)) > diff:
        oldguess = newguess
        newguess = (oldguess + number/oldguess)/2.0
        tries = tries + 1
        calc = newguess
    actDiff = abs((math.sqrt(number) - calc)) 
    return calc, actDiff, tries

def printResults(number, diff, calc, actDiff, tries):
    print("For the square root of", number, "after", tries, "tries")
    print("The calculated square root is {:0.11f}".format(calc))
    print("The real square root is       {:0.11f}".format(math.sqrt(number)))
    print("The difference is             {:0.11f}".format(actDiff))
    print("The delta was                 {:0.11f}".format(diff))
    print()


if(__name__=='__main__'): main()
