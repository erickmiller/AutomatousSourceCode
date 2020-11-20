# Project Euler Problem 9: Find the product of a, b and c in the 
# pythagorean triplet a^2 + b^2 = c^2 and a + b + c = 1000
# 
# Judith Gammie
# 6th July 2015

import math
def pythag_triplets():
    for i in range (1,1000):
        for j in range (i,1000):
            k_squared = (i*i) + (j*j)
            if (is_square(k_squared) and i + j + math.sqrt(k_squared) == 1000):
                print i * j * math.sqrt(k_squared)
                break

def is_square(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False

pythag_triplets()
