#!/usr/bin/env python

"""
This script is an implementation of Heron's Method (cs.utep.edu/vladik/2009/olg09-05a.pdf), one of the oldest ways of
calculating square roots by hand.
The script asks for maximum number of iterations to run, the square root to approximate, and the initial guess
for the square root. Each successive guess is closer to the square root until either the maximum number of iterations
is reached or the actual square root is found.
"""

__author__ = 'Carlos A. Gomez'


def ask_and_approx_roots():
    num_iterations = int(input("Please enter the number of iterations (an integer): "))
    square_root_to_approx = int(input("Please enter the square root to approximate (an integer): "))
    sq_root_guess = float(input("Please enter a guess for the square root: "))
    return heron_method(num_iterations, square_root_to_approx, sq_root_guess)


def heron_method(num_iterations, square_root_to_approx, sq_root_guess):
    sq_root_approximation = 1/2 * (sq_root_guess + square_root_to_approx/sq_root_guess)
    result_found = False
    run_counter = 0
    while not result_found:
        run_counter += 1
        last_guess = sq_root_approximation
        print("Guess number " + str(run_counter) + " is " + str(sq_root_approximation))
        sq_root_approximation = 1/2 * (sq_root_approximation + square_root_to_approx/sq_root_approximation)
        if abs(sq_root_approximation - last_guess) == 0 or run_counter == num_iterations:
                result_found = True
    print("The best guess for the square root, using " + str(run_counter) + " iterations, is "
          + str(sq_root_approximation))


if __name__ == '__main__':
    ask_and_approx_roots()
