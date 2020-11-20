import math
import utils

def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))


def add(u, v):
    a = []
    if abs(len(u) - len(v)) < 1e-12:
        a = [sum(x) for x in zip(u, v)] 
    else:
        utils.error('Vectors are of different length (utils_math: add)')
    return a


def sub(u, v):
    a = []
    if abs(len(u) - len(v)) < 1e-12:
        a = [ u[i]-v[i] for i in range(len(u)) ]
    else:
        utils.error('Vectors are of different length (utils_math: sub)')
    return a


def dot(u, v):    
    a = []
    if abs(len(u) - len(v)) < 1e-12:
        a = [ sum(u[i]*v[i] for i in range(len(u))) ]
        print '\n', a, '\n'
    else:
        utils.error('Vectors are of different length (utils_math: dot)')
    return a


def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag  for i in range(len(v)) ]
    

def squareRoot(list):
    return map(lambda x: math.sqrt(x), list)    


def square(list):
    return map(lambda x: x ** 2.0, list)

def fft(signal):
   n = len(signal)
   if n == 1:
      return signal
   else:
      Feven = fft([signal[i] for i in xrange(0, n, 2)])
      Fodd = fft([signal[i] for i in xrange(1, n, 2)])
 
      combined = [0] * n
      for m in xrange(n/2):
         combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
         combined[m + n/2] = Feven[m] - omega(n, -m) * Fodd[m]
 
      return combined
