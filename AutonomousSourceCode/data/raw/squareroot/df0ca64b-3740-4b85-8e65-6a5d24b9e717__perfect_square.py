"""
File Name: Ch2_Ex10.py
Developer: Justin A. Shores
Date Last Modified: 09/02/2014
Description: Prompt user for a number
 	     Print whether number is a perfect square
	     If not ask for another number
"""
import math

# is the number a perfect square?
def is_perfect_square(integer):
        number_root = math.sqrt(integer) + 0.5 # add .5 to avoid base value err.
        if (int(number_root) ** 2) == integer:
                return False # is perfect square
        else:
                return True # not perfect square

# while user does not enter perfect square
while True:
	# get number
	number_str = input("Enter a number that you believe is a perfect square: ")
	number_int = int(number_str)

	# check if perfect square and try again
	if is_perfect_square(number_int) == False:
		print("The number " + str(number_int) + " is a perfect square!")
		break #user entered perfect square
	else:
		print("Sorry try again! " + str(number_int) + " isn't a perfect square")
