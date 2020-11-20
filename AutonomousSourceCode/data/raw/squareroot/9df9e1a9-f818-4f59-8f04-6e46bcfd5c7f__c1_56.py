#56) Given a int number, write code to judge the number of all its factor is an even number or an odd number
import math

def isPerfectSquare(num):
	squareRoot = math.sqrt(num)
	return squareRoot**2 == num

def countEvenOrOddFactors(num):
	if isPerfectSquare(num):
		return "Odd number of factors"
	else:
		return "Even number of factors"


def main():
	num = input("Enter the number")
	print countEvenOrOddFactors(num)

main()