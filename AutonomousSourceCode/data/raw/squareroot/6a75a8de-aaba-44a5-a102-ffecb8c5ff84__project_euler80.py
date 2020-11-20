# Square root digital expansion
"""
It is well known that if the square root of a natural number 
is not an integer, then it is irrational. The decimal
expansion of such square roots is infinite without 
any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and 
the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of 
the digital sums of the first one hundred decimal digits
for all the irrational square roots.
"""


def digit_sum_sqrt(n):
    square_root = str(int(n ** 0.5))
    for i in range(1, 100):
        for j in range(10):
            if (int(square_root) * 10 + j) ** 2 > n * 10 ** (2 * i):
                square_root += str(j - 1)
                break
            if j == 9:
                square_root += str(j)

    s = sum(map(int, square_root))
    # print(n, s)
    return s


def main():
    non_perfect_square = [i for i in range(1, 101) if int(i ** 0.5) ** 2 != i]
    print(sum(map(digit_sum_sqrt, non_perfect_square)))


if __name__ == '__main__':
    from time import time
    starting_time = time()
    main()
    print("Time elapsed:", time() - starting_time, "seconds")
