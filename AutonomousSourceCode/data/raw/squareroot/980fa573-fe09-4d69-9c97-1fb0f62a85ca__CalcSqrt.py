#  File: CalcSqrt.py

#  Description: Calculate the square root of a number and display it

#  Student Name: Collin Murphy

#  Student UT EID: cbm772

#  Course Name: CS 303E

#  Unique Number: 52680

#  Date Created: 15 Oct 2012

#  Date Last Modified: 15 Oct 2012

def sqrt(n):
  '''function to determine the square root of a given numebr n'''

  #set initial values
  error = 1
  oldGuess = n / 2
  newGuess = 0

  #perform computation
  while (error > 1e-6):
    newGuess = ((n / oldGuess) + oldGuess) / 2
    error = abs(oldGuess - newGuess)
    oldGuess= newGuess

  #return result
  return newGuess

def main():
  '''main function to test square root function'''

  #get user input until it is valid
  n = -1
  while (n <= 0):
    n = eval(input("Enter a positive number: "))
    print()

  #calculate square root
  result = sqrt(n)

  #print result
  print("Square root is: %s" %format(result, '0.12g'), end = '\n\n')
  print("Difference is: %s" %format((result - n ** 0.5), '0.1f'))

main()
