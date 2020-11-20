import fractions

def squareRootConvergents():
    count = 1
    numberCount = 0
    x = 2 + fractions.Fraction(1,2)
    while count < 999:
        y = 1 + 1 / x
        if len(str(y).split('/')[0]) > len(str(y).split('/')[1]):
            numberCount += 1
        x = 2 + 1 / x
        count += 1
    return numberCount
print squareRootConvergents()
