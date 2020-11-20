"""
This simple Python script embodies its namesake by acting as a
basic calculator. Currently, It can perform addition, subtraction,
division, multiplication, exponentiation, and square roots. More
functions may be added at a later date, or you could add your own!
"""

from __future__ import division # Importing the proper modules
from math import sqrt

print "Welcome to my basic calculator program!" # Welcome statement

def add(x, y): # Addition function
    s = x + y
    return "\n\t{} + {} = {}".format(x, y, s)
    
def minus(x, y): # Subtraction function
    s = x - y
    return "\n\t{} - {} = {}".format(x, y, s)
    
def division(x, y): # Division function
    s = x / y
    return "\n\t{} / {} = {}".format(x, y, s)
    
def multiplication(x, y): # Multiplication function
    s = x * y
    return "\n\t{} * {} = {}".format(x, y, s)
    
def exponentiation(x, y): # Exponentiation function
    s = x ** y
    return "\n\t{} ** {} = {}".format(x, y, s)
    
def squareRoot(x): # Square root function
    s = sqrt(x)
    return "\n\t√{} = {}".format(x, s)
    
while True:
    c = raw_input("\nPlease pick an operation by number:\n\t1. Addition (+)" \
    "\n\t2. Subtraction (-) \n\t3. Division (/)\n\t4. Multiplication (*)" \
    "\n\t5. Exponentiation (**) \n\t6. Square Root (√)")
    if c in ["1", "2", "3", "4", "5", "6"]: # Ensuring that only the listed options are inputted
        break
    else:
        print"\nChoose a number (1, 2, 3, 4, 5, 6) for your intended operation." # Error message
        continue

while True:
    try:
        a = raw_input("\nChoose your first number: ")
        ia  = float(a)
    except ValueError:
        print "\nNegative/positve integers or decimals only." # Only options allowed
        continue
    else:
        break
    
while True and c != "6":
    try:
        b = raw_input("\nChoose your second number: ")
        ib = float(b)
    except ValueError:
        print "\nNegative/positive integers or decimals only." # Only options allowed
        continue
    else:
        break

if c == "1": # Calling on the proper function
    print add(ia, ib)
elif c == "2":
    print minus(ia, ib)
elif c == "3":
    print division(ia, ib)
elif c == "4":
    print multiplication(ia, ib)
elif c == "5":
    print exponentiation(ia, ib)
elif c == "6":
    print squareRoot(ia)
