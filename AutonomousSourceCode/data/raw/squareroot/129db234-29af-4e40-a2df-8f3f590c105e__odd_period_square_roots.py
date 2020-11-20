import math

def get_continued_fraction(square_root_argument):
  first_appearance = {}
  sequence = []
  square_root_floor = int(math.sqrt(square_root_argument))
  if square_root_floor ** 2 == square_root_argument:
    return [square_root_floor], []
  a, b, c = square_root_floor, square_root_floor, 1
  while (a, b, c) not in first_appearance:
    first_appearance[a, b, c] = len(sequence)
    sequence.append(a)
    c = (square_root_argument - b ** 2) / c
    a = int((math.sqrt(square_root_argument) + b) / c)
    b = -(b - a * c)
  index = first_appearance[a, b, c]
  return sequence[:index], sequence[index:]

def main():
  odd_period_count = 0
  max_period = 0
  max_period_argument = 0
  for n in xrange(10001):
    period = len(get_continued_fraction(n)[1])
    if period > max_period:
      max_period = period
      max_period_argument = n
    if period % 2 == 1:
      odd_period_count += 1
  return odd_period_count

if __name__ == '__main__': print main()
