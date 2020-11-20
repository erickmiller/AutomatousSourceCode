from fractions import Fraction
from numlib import is_square
def get_digit_square_root(n, num_digit = 2):
	if num_digit == 0:
		return Fraction(int(n**0.5))
	else:
		base = get_digit_square_root(n, num_digit - 1)
		denominator = 10**num_digit
		d = 1
		while (base + Fraction(d,denominator))**2 <= n:
			d += 1
		return base + Fraction(d - 1, denominator)

def count_first_n_digit(f, n = 100):
	denominator = f.denominator
	m = int(f) + n
	mult = 10**m / f.denominator
	numerator = str(f.numerator * mult)
	s = 0
	for i in range(n):
		s += int(numerator[i])
	return s

def main():
	s = 0
	for n in range(1, 101):
		if not(is_square(n)):
			f = get_digit_square_root(n, 100)
			print n, f
			s += count_first_n_digit(f)
			print count_first_n_digit(f), f
	print "count:", s

main()