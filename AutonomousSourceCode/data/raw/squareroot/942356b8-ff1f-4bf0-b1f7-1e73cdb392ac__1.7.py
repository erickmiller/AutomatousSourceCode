import math
import argparse
import sys

def sqrt(x):
    def avg(*args):
        return float(reduce(lambda x,y: x+y, args))/len(args)

    def improve(guess, x):
      return avg(x/guess, guess)

    def guess_change_is_small_fraction_of_guess(guess, x):
        return math.fabs(improve(guess, x) - guess) < guess * 0.0001

    def good_enough(guess, x):
        return guess_change_is_small_fraction_of_guess(guess, x)

    def sqrt_iter(guess, x, calls=0):
        if good_enough(guess, x):
            return guess
        else:
            return sqrt_iter(improve(guess, x), x, calls=calls)

    return sqrt_iter(1.0, x)

parser = argparse.ArgumentParser(description = 'Find square root of a number using\
                                 Newton\'s approximation method')
parser.add_argument('NUM')

if __name__ == "__main__":
    parsed = parser.parse_args(sys.argv[1:])
    print sqrt(parsed.NUM)
