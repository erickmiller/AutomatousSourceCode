'''
newton_root.py

Author: Patrick Rummage
        [patrickbrummage@gmail.com]

Objective:
    Define a function that runs in a loop calculating
    successive approximations of the square root of
    a number, using Newton's method. Returns a result
    within the range of one epsilon.
'''

def find_root(a, eps):
    appx = a / 2.0
    while True:
        root = (appx + a/appx) / 2

        if abs(appx - root) < eps:
            break
        appx = root
    return root

epsilon = 0.0000001
print find_root(25, epsilon)
print find_root(64, epsilon)
print find_root(2, epsilon)
