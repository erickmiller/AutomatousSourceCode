#! /usr/bin/env python3

import math

def isSquare(a) :
	return math.sqrt(a) == float(math.floor(math.sqrt(a)))


def squareRootDigitByDigit (number, numberOfDigits) :

	squareRootResult = 0

	numberRest = number
	remainder = 0

	digit = 0
	while digit < numberOfDigits  :

		c = 0

		if numberRest != 0 :
			log10OfRest = math.floor(math.log10(numberRest))

			if log10OfRest % 2 == 1 :
				log10OfRest -= 1

			magnitudeOfRest = int(math.pow(10,log10OfRest))

			#if numberRest > 9 :
			#	magnitudeOfRest /= 10
			

			c = int(numberRest / magnitudeOfRest)

			numberRest -= c*magnitudeOfRest

		else :
			numberRest = 0
		

		c += remainder*100




		# c is prepared

		p = squareRootResult

		# p is prepared

		y = c
		x = 0
		while y <= c :

			y = (20*p + x) * x

			x += 1

		x -= 2
		y = (20*p + x) * x

		# x,y is prepared

		remainder = c - y

		squareRootResult = squareRootResult*10 + x

		#print("c",c, "rest",numberRest, "mag",magnitudeOfRest, "p",p, "x",x, "y",y, "->", squareRootResult)



		digit += 1


	return squareRootResult


def digitSum (number) :

	sum = 0
	rest = number

	while len(rest) > 0 :

		digit = int(rest[0])
		rest = rest[1:]

		sum += digit

	return sum


sumsum = 0

i = 2
while i < 101 :

	if isSquare(i) == False :

		digits = squareRootDigitByDigit(i,100)

		sum = digitSum(digits.__str__())

		sumsum += sum

		print(i, ":", sum, digits)

	i += 1


print(sumsum)

