from decimal import getcontext, Decimal


def solver(n=100, m=100):
    """ For the first n natural numbers, find the total of the digital sums
    of the first m decimal digits for all the irrational square roots.
        
    (solved 2014-11-26)
    """
    result = 0
    getcontext().prec = m + 2  # set precision
    for number in range(n + 1):
        square_root = Decimal(number).sqrt()  # compute square root
        if square_root % 1:  # if square_root is not a perfect square
            # Get m precision of decimal places and sum them up for each number
            decimal_places = str(square_root).replace(".", "")[:m]
            result += sum(int(digit) for digit in decimal_places)
    return result
    
solver()