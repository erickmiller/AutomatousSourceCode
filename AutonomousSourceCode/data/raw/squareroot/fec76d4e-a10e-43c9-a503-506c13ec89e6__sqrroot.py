'''
Created on 31 May 2015

@author: Piers
'''
import unittest

def difference_is_less_than(number_1, number_2, precision):
    print number_1, number_2, precision, abs(number_1 - number_2)
    return abs(number_1-number_2) <= precision

def decirange(start, stop, step_size):
    i = float(start)
    while True:
        print 'yielding %s' % i
        yield i
        i += float(step_size)
        if i > stop:
            raise StopIteration()

def sqr_root(number, precision):
    """return an approximation of the square root of number
    
    precision is the max difference between the real square root and the value returned
    e.g. sqr_root(1.44,1) = 1
    sqr_root(1.44, 0.1) = 1.2
    """
    
    for guess in decirange(1,number,0.05):
        print guess
        square = guess*guess
        if difference_is_less_than(square, number, precision):
            break
    return guess

class TestSqrRoot(unittest.TestCase):
    def test_15_1(self):
        self.assertEqual(sqr_root(15,1), 4)
         
    def test_15_2(self):
        self.assertEqual(sqr_root(15,0.1), 3.9)
         
#     def test_169_1(self):
#         self.assertEqual(sqr_root(169,0.1), 13)

# class TestDecirange(unittest.TestCase):
#     def test_simple(self):
#         for i in decirange(1,2,0.1):
#             print i