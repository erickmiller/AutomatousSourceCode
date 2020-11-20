from math import sqrt, factorial, pi
import sys


def square_root(a, x, iteration=0):
    a = float(a)
    if abs(x - sqrt(a)) > 0.000001:  # Checks how accurate the guess(x) is
        next_x = ((x + (a / x)) / 2)  # Newton's Method, readjusts guess(x) every time it's run
        iteration += 1
        return square_root(a, next_x, iteration)
    # print "Number of iterations: %i" % iteration
    return x


def table_print(a, calculated_square_root):
    internal_square_root = sqrt(a)
    difference = abs(calculated_square_root - internal_square_root)
    is_difference = difference < 0.000001
    sys.stdout.write("{:<3}{:<20}{:<20}{:<20}{:<20}\n".format(a, calculated_square_root,
                                                              calculated_square_root,
                                                              difference,
                                                              is_difference))



# result = square_root(9, 100)
sys.stdout.write("{:<3}{:<20}{:<20}{:<20}{:<20}\n".format('n', "square_root",
                 "math.sqrt", "difference", "is difference < 0.000001?"))

table_print(1, square_root(1, 1))
table_print(2, square_root(2, 2))
table_print(3, square_root(3, 2))
table_print(4, square_root(4, 2))
table_print(5, square_root(5, 2))
table_print(6, square_root(6, 3))
table_print(7, square_root(7, 3))
table_print(8, square_root(8, 3))
table_print(9, square_root(9, 3))

left = (2 * sqrt(2)) / 9801
answer = 0
k = 0
while not(abs(answer - (1 / pi)) < 0.000001):
    right_top = (factorial(4 * k)) * (1103 + (26390.0 * k))
    right_bottom = (factorial(k) ** 4) * (396 ** (4 * k))
    right = right_top / right_bottom
    answer = right * left
    k += 1

print answer