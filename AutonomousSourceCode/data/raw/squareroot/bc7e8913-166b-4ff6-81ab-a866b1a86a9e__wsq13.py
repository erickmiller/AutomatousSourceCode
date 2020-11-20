import math

def squareroot(n):
    x = n
    e = 0.0000001
    y = 1
    while (x - y > e):
        x = (x + y) / 2
        y = n / x
    return x


number = float(input("Enter the number that you want to know the square root please: " ))

calcul_squareroot = squareroot(number)
print (calcul_squareroot)
