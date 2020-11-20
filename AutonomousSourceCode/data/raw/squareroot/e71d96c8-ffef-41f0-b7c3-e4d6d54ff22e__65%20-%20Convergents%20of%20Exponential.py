execfile("16 - Power Digit Sum.py")
execfile("57 - Square Root Convergents.py")

def fracs(array):    # Finds the fractions of continuous expansion
    a = array
    f = frac(a[-2], 1, 1, a[-1])
    a = a[:-2]
    while a:
        f = frac(a[-1], 1, f[1], f[0])
        a = a[:-1]
    return tuple(f)

def exp(r):
    e = [1, 1, 2]
    while len(e) < r:
        if (e[-1] + e[-2]) % 2 == 0:
            e.append(e[-1] + e[-2] + e[-3])
        else:
            e.append(1)
    e[0] = 2
    return fracs(e)

# n = 100
# f = exp(n)
# s = sumup(f[0])
# print "The sum of digits in the numerator of", str(n) + 'th convergent is:', s
