"""
Program that asks the user for a positive number and then outputs the
approximated square root of the number. Use Newton's method to find the
square root, with epsilon = 0.01. (Epsilon is the allowed error, plus or
minus, when you square your calculated square root and compare it to
your original number.)
"""


def ask_for_number():
    """Asks user for a positive number"""
    number = 0
    while True:
        if number > 0:
            return number
        try:
            number = int(input("Please provide a positive nuumber: "))
        except:
            pass


def newtons_method(num, guess=None):
    """Calculates the square root of a number."""
    if guess is None:
        # picked 20 out of thin air. Let me know if I should change.
        guess = 20

    new_guess = .5*(num/guess+guess)

    if new_guess == guess:
        print("The square root of {} is {}.".format(num, guess))
    else:
        newtons_method(num, new_guess)

newtons_method(num=ask_for_number())
