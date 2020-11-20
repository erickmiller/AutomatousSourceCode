import math 

def divisors(p):
    divs = [1]
    square_root = int(math.ceil(math.sqrt(p))) 
    for x in xrange(2, square_root):
        if p % x == 0:
            div1 = x
            div2 = p/x

            divs.append(div1)
            if div1 != div2:
                divs.append(div2)

    return divs

sum_of_amicable = 0
for x in range(10000):
    sum_of_divs = sum(divisors(x))
    if x == sum_of_divs:
        continue

    if x > sum_of_divs:
        continue

    reverse = sum(divisors(sum_of_divs))

    if reverse == x:
        sum_of_amicable += sum_of_divs
        sum_of_amicable += x

print sum_of_amicable
