low = 1
upper = 100
prec = 1000

# http://en.wikipedia.org/wiki/Integer_square_root
# Use Newton's method
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def count_digits_in_sqrt(num):
    return sum(map(int, str(isqrt(num * 10 ** (2 * (prec - 1))))))

total = 0
rational_root = 1
for curr in xrange(low, upper+1):
    if rational_root ** 2 != curr:
        total += count_digits_in_sqrt(curr)
    else:
        rational_root += 1

print total
