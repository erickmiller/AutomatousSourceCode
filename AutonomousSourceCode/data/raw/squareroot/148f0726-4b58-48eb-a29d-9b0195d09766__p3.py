import math

def is_prime(num):
    
    for i in range(2, num/2):
        if num % i == 0:
            return False
    
    return True

def highest_factor(num):
    square_root = int(math.sqrt(num))
    
    for i in reversed(range(2,square_root)):
      if num % i == 0:
          if is_prime(i):
              return i
              
print highest_factor(600851475143)