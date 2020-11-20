"""
Clifton Crosland
Project Euler 206 - Find the concealed square - 1_2_3_4_5_6_7_8_9_0
"""
import math

DIGITS = [1,2,3,4,5,6,7,8,9,0]

def is_concealed_number(n):
  matches = 0
  while n != 0:
    digit = n % 10
    if digit != DIGITS[10 - 1 - matches]:
      return False
    matches += 1
    n /= 100
  return matches == 10
  
def main():
  MIN = 1020304050607080900
  MAX = 1929394959697989990
  root = int(math.sqrt(MIN))
  while True:
    if root % 100 == 30 or root % 100 == 70:
      square = root * root
      # Since the square ends in a 0, then the root must be a multiple of 10.
      # Hence, the square must be a multiple of 100.  Since the third to last digit
      # of the square is a 9, then the square must end in 900.  We can get 900 if
      # the last two digits of the root are 30 or 70 (30^2 = 900, 70^2 = 4900).
      if square % 1000 == 900:
        if is_concealed_number(square):
          print "Rock on!"
          print "square = %d, root = %d" % (square, root)
          return
    root += 10
  
if __name__ == "__main__":
  main()