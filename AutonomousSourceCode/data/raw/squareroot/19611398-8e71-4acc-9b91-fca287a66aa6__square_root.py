# Heron of Alexandria documented a methon to compute the square root
# we are going to write a program to do the same - how exciting :)


def squareRoot(x):
    g = x/2.0
    while True:
        g = (g + x/g)/2.0
        if (abs(x - g**2) <= 0.001):
            break
    return g

while True:
    try:
        num = int(raw_input("Enter integer: "))
        break
    except ValueError:
        print 'Invalid Integer!! Please Try Again...'

sroot = squareRoot(num)
sroot = round(sroot, 3)
print "square root of {0}: {1}".format(num, sroot)
