def squareRoot(a):
    for number in range (1,a):
        if a**2 == a:
            return "square root of" + str(a) + "would be" + str(number)
        return "Square root "+ str(a) + " isn't " + str(number)
