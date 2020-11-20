'''
name: Joshua Rodriguez
email: ewized@gmail.com
file: perfect_square.py
problem: chapter 2 number 10 page 145
description: Write a short program that will
    * prompt the user for a number
    * print out whether the number is a perfect square
    * prompt the user for another number if the number is now a perfect square
'''
import math

is_square = input("Enter a number: ")

def is_perfect_square(is_square):
    root = math.sqrt(int(is_square))
    return int(root) ** 2 == int(is_square)

while not is_perfect_square(is_square):
    #print(str(is_square))
    is_square = input("That was not a perfect square, enter another number: ")
else:
    print(str(is_square) + " was a perfect square well done!")
