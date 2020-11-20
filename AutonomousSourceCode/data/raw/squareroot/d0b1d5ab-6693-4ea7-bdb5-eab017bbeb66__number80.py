"""
David Schonberger
Project Euler - problem 80
Square root digital expansion
"""

import datetime
import decimal
pr = 110
decimal.getcontext().prec = pr

def is_square(n):
    if(n == 1):
        return True
    else:
        i = 1
        while(i ** 2 < n):
            i += 1
        if(i**2 == n):
            return True
        else:
            return False

bef = datetime.datetime.now()
n = 100
upper = 100
digit_total = 0
sum_of_digital_sums = 0
for i in range(1,n + 1):
    if(not is_square(i)):
        num = str(decimal.Decimal(i).sqrt())
        d1 = int(num[0])
        r = num[2 : upper + 1]
        digit_total += sum([int(ch) for ch in r]) + d1
    
print "\n", digit_total
aft = datetime.datetime.now()
