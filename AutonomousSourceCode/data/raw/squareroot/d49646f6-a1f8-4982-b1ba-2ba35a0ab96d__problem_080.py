"""problem_080.py

Problem 80: Square root digital expansion

It is well known that if the square root of a natural number is not an integer,
then it is irrational. The decimal expansion of such square roots is infinite
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the
first one hundred decimal digits is 475.

For the first NUM_COUNT natural numbers, find the total of the digital sums of
the first DIGIT_COUNT decimal digits for all the irrational square roots.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

NUM_COUNT = 100 # default: 100
DIGIT_COUNT = 100 # default: 100

# SOLUTION ####################################################################

def solve():
    total = 0
    for n in range(2, NUM_COUNT + 1):
        if com.is_square(n):
            continue

        root = com.sqrt_expansion(n, DIGIT_COUNT)
        root = root.replace('.', '')
        total += sum([int(digit) for digit in root[:DIGIT_COUNT]])

    return total


if __name__ == '__main__':
    print(solve())
