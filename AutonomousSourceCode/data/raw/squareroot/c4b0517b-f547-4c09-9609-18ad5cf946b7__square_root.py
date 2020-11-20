"""A program that asks the user for a positive number and then outputs the approximated square root of the number."""
while True:
    try:
        num = float(input('Please input a number:  '))
        break
    except:
        print("ERROR: Input not a number")
        continue

#print(num)

def sq_rt (num):
    """Approximates square root of parameter to 2 decimal places"""
    neg=""
    if num < 0:
        num = abs(num)
        neg = 'i'
    guess_1 = 1
    guess_2 = 0
    count = 0
    while round(guess_1, 2) != round(guess_2, 2):
        count += 1
        guess_2 = guess_1
        guess_1 = (guess_1 + num/guess_1)/2
        print("This loop has iterated", count, "times and the current guess is", str(guess_1)+".")
    return (str(round(guess_1,2))+neg)

print("The square root of", num, "is", sq_rt(num))
