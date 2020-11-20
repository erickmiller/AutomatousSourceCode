__author__ = 'jeremy.sandbergtobel'

def add(term1, term2):
    result = term1 + term2
    return result

def subtract(term1, term2):
    result = term1 - term2
    return result

def multiply(factor1, factor2):
    product = factor1 * factor2
    return product

def square(value):
    product = value * value
    return product

def square_of_square_root(value):
    import math
    root = value ** 2
    product = math.sqrt(root)
    return product

print square_of_square_root(value=(-16))
