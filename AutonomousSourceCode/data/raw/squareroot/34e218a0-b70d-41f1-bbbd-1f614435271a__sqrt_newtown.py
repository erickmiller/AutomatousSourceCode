#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""


def main():
    print(square_root(2))

def square_root(x):
    guess = 1.0
    while not is_good_enough(guess, x):
        guess = improve(guess, x)
        print(guess)
    return guess

def improve(guess, x):
    q = (x*1.0)/guess
    return average(q, guess)

def average(x, y):
    return (x+y)/2.0

def is_good_enough(guess, x):
    return abs(improve(guess, x) - guess) < 0.0001
    #return abs(guess**2 - x) < 0.0001

if __name__ == '__main__':
    main()

