# Using bisection search to approximate square root
def squareRoot(x, epsilon):
    low = 0.0
    high = max(1.0, x)

    ans = low + (high-low)/2.0

    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = low + (high-low)/2.0
    return ans

x = int(raw_input('Enter Integer: '))
epsilon = 0.001
sroot = squareRoot(x, epsilon)

print 'square root of {} is: {}'.format(x, round(sroot, 3))
