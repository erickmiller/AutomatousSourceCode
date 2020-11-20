#a program to determine prime numbers

from math import sqrt

def divide(n):
	return n % 2

def question():
	#var for natural number user inputs
	return eval(input("Please provide a natural number: "))

def division(n):
	#creates the square root
	squareRoot = sqrt(n)
	#create the var to use as a counter
	count = squareRoot

	#iterate until the count drops to two
	while count >= 2:
		#decide if the number is even
		if (n/count) % 2 == 0:
			return False #return False since n is not prime
		count = count - 1 #decrement the count by one
	return True #if n never evaluates as even then return True

def displayPrime(evenOdd):
	#decide if the evenOdd var is True
	if evenOdd == True:
		print("The number is prime") #print the evenOdd value is prime
	else:
		print("The number is even")

def main():

	#create var isPrime from the division function
	isPrime = division(question())

	#call the displayPrime function to show if the number is even or odd
	displayPrime(isPrime)

main()