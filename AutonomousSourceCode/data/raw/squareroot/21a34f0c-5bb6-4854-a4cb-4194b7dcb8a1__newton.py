# from math import sqrt

__author__ = 'Shane'
# Uses Newton's Method to estimate the square root of a positive number


def mysqrt(n, x):
    if abs(n - x ** 2) < 0.0000000000001:
        return x
    else:
        x = (x + n / x) / 2
        return mysqrt(n, x)


def main():
    a = 0
    while a <= 0:
        a = float(input("Enter a number: "))
        if a <= 0:
            print("")
            print("Please enter a positive number!")
    sqrta = mysqrt(a, 1)
    print("")
    print("The square root of", a, "is about", sqrta)
    # print("Error: ", sqrta - sqrt(a))

main()

'''
# To display a list:
for i in range(1,21):
    print("The square root of", i, "is about", mysqrt(i, 1))
'''
