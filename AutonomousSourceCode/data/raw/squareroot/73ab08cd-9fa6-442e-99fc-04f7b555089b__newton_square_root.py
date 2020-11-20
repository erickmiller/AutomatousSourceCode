# Write a function called mySqrt that will approximate the square root of a number, call it n, by using Newton’s 
# algorithm. Newton’s approach is an iterative guessing algorithm where the initial guess is n/2 and each 
# subsequent guess is computed using the formula: newguess = (1/2) * (oldguess + (n/oldguess)).

def mySqrt(a):
	guess = 0
	guess = a/2
	for i in range(6):											# Use 5 guesses only 
		newguess = (guess + a/guess)/2
		guess = newguess
	return guess

stdin = input("Please enter a number: ")
n = float(stdin)
print("The estimated positive square root of", n, "is", mySqrt(n))