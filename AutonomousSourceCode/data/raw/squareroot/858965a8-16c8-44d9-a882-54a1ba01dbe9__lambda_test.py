import math

def square_root(x):
    return math.sqrt(x)

sq_root = lambda x : math.sqrt(x)


print('square root of {} is {}'.format(64,square_root(64)))
print('square root of {} is {}'.format(64,sq_root(64)))
