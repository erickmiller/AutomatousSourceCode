# Python Code for Square Root

num = int(input("Enter a positive number: "))

def newtonest(num):
    return num ** 0.5

def estimate(num):
    guess = num/3
    count = 0
    epsilon = 0.01
    sq_guess = ((num / guess) + guess)/2
    while abs(newtonest(num) - sq_guess) > epsilon:
        newguess = sq_guess
        sq_guess = ((num / newguess) + newguess)/2
        count +=1
    print("The square root of {} is {} with {} interations.".format(num,sq_guess,count))

estimate(num)
