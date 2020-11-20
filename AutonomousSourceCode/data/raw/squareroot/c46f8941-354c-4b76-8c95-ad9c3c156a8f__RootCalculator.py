x = 0
root = 0
def squareRoot(x, maxPrecision, root):
    precision = maxPrecision
    low = 0.0
    high = x
    guess = (low + high)/2
    while (precision > 0):
        if guess**root > x:
            high = guess
        else:
            low = guess
        guess = (low + high)/2
        precision -= 1
    return guess
while True:
    x = float(raw_input('Enter a number: '))
    root = int(raw_input('Enter a number: '))
    if root <= 10:
        if root == 1:
            print('The first root of ' + str(x) + ' is about ' + str(squareRoot(x, 1000000, root)))
        elif root == 2:
            print('The square root of ' + str(x) + ' is about ' + str(squareRoot(x, 1000000, root)))
        elif root == 3:
            print('The cube root of ' + str(x) + ' is about ' + str(squareRoot(x, 1000000, root)))
        else:
            print('The ' + str(root) + 'th root of ' + str(x) + ' is about ' + str(squareRoot(x, 1000000, root)))
    else:
        print 'The exponent was too small!'