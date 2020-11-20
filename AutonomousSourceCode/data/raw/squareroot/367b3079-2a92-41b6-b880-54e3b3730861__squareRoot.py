# import math

def closeEnough(num1,num2):
	if (abs(num1-num2) < 0.001):
		return True
	else:
		return False

def squareRoot(num,guess):
	# guess = 1
	if(closeEnough((num/guess),guess)):
		print round(guess,4)
	else:
		guess = ((num/guess)+guess)/2
		squareRoot(num,guess)

if __name__ == '__main__':
	
	num = input("Enter number:")
	
	squareRoot(float(num),1.0)
