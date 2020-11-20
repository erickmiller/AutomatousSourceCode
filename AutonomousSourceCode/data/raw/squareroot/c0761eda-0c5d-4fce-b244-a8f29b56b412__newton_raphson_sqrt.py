
# Newton-Raphson for square root of a number

number = float(raw_input("Enter a positive number: "))

def newton_raphson_sqrt(number):
  epsilon = 0.01
  y = number
  guess = y/2.0

  while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
    #print(guess)

  return guess

print('Square root of ' + str(number) + ' is about ' + str(newton_raphson_sqrt(number)))