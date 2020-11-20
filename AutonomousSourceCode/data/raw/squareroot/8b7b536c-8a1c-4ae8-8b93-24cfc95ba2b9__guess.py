#!/usr/bin/python

def nextGuess(guess, x):
	next_guess = (guess + (x/guess)) / 2
	return next_guess
	
def main():
	guess = int(input("Enter a guess for what the square root might be: "))
	x = int(input("Enter the number you want the root of: "))
	print("The next guess is {}".format(nextGuess(guess, x)))
	
if __name__ == "__main__":
	main()