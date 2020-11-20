def getSortedDigits(number):
    digits = list()
    k = 0
    while number // 10**k > 0:
        digits.append(number%10**(k+1)//10**k)
        k += 1

    digits.sort()
    digits.reverse()

    number = 0
    for k in range(len(digits)):
        number += digits[k]*10**(len(digits)-k-1)

    return number

powers = dict()
k = 1

while True:
    sortedDigits = getSortedDigits(k**3)
    try:
        powers[sortedDigits].append(k)
        if len(powers[sortedDigits]) >= 5:
            print(powers[sortedDigits][0]**3)
            break
    except KeyError:
        powers[sortedDigits] = [k]

    k += 1