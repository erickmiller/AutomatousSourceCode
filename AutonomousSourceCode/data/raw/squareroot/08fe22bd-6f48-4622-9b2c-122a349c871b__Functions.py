__author__ = 'student'


import math

class Function:
    def __init__(self, key, header, explanation, compute):
        self.key = key
        self.header = header
        self.explanation = explanation
        self.compute = compute

def sqrt(x):
    return math.sqrt(x)

function_list = [
    Function('sqrt', 'SQRT', "Square root function", sqrt),
    Function('sqr', "Square", "Square of the argument", (lambda x : x*x)),
    Function('log2', "Log2", "Binary logarithm", (lambda x : math.log2(x))),
    Function('cube', "Cube", "Cube of the argument", (lambda x: x*x*x))
    ]

def getFunctionByKey(key):
    for func in function_list:
        if key == func.key:
            return func
