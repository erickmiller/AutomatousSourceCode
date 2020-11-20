"""
This script allows the user to find the square root of a number.
"""

def squareroot(number):
    estimate = number / 2
    epsilon = 0.000000000001

    while True:
        # print estimate
        root = 0.5 * (estimate + number / estimate)
        if abs(root - estimate) < epsilon:
            return root
        else:
            estimate = root

if __name__ == "__main__":
    number = float(raw_input("What would you like to find the square root of?\n"))
    print squareroot(number)