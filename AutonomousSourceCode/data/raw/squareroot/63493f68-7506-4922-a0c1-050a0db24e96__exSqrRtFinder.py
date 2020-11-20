def exSqrRt(number):
    
    float(number)
    counter = 1.0
    
    while counter**2 == number:
        return str(counter) + 'is the square root of' + number
    else:
        counter += 0.0001
        exSqrRt(number)