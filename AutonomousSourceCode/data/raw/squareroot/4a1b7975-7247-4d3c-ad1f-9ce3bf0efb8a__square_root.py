def squareroot(number):
    difference = 1
    number_guess = float(number/2)
    while difference > 0.01:
        square_root = number_guess - ((number_guess*number_guess - number) / (2*number_guess))
        difference = float(abs(number_guess - square_root))
        number_guess = square_root
    return round(square_root, 3)

def root(number, exp):
    i = exp - 1
    if i > 0:
        root1 = squareroot(number)
        return root(root1, exp - 1)
    else:
        return number

print(root(1012312, 1))