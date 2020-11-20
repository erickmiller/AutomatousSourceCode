def iterSqRt(number):
    for counter in range(1, number):
        if counter**2 == number:
            return "square root of" + str(number)+ "is" + str(counter)
            return "Failed" + str(number) + "SqRt is not an interger"