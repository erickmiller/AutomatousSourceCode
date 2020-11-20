import sys
from math import sqrt
import itertools as it

def flatten1(m):
    return sum(m, [])


def isNoComment(line):
    return not line.startswith('*')


def isLinearity(line):
    return line.startswith('linearity')
def getLinearity(line):
    return int(line.split()[1])

def getFacettes(flines):
    began = False
    for line in flines:
        if 'end' in line:
            return
#        print line
        if began:
            yield line
        if 'begin' in line:
            began = True



def squareRoot (n):

    a = int(sqrt(n - 1))
    if a*a + 1 != n:
        print "length %s not square" % (n-1)
    return a
def triRoot (n):
    a = -0.5 + sqrt(0.25 + 2*n)
    if a != int (a):
        print "warnin:", n, " not triangular"
    return int(a)
    


def squareIt (line):
#    print line
#    print line.split()
    numbers = map(int, line.split())
    n = len(numbers)
    a = triRoot(n)
    beta = numbers[0]
    m = [numbers[1:][y*a:(y+1)*a] for y in range(a)]
    s = ''.join([''.join(['% i '% num for num in line])+'\n' for line in m])
    return s, "% i" % beta

def squareTri(numbers):
    n = len(numbers)
    a = triRoot(n)
    numbers = ['% i '% num for num in numbers]
    m = [numbers[y*(y+1)/2:(y+1)*(y+2)/2]+(a-y-1)*[' . '] for y in range(a)]
    s = ''.join([''.join(line)+'\n' for line in m])
    return s



def triCo(numbers, x,y):
    c = y * (y+1)/2 + x
    if x <= y and c < len(numbers):
        return numbers [c]
    else:
        return None
#d = {0:'.', None: ' ', 1:'+', -1:'-'}

dd = {(0,0): '.  ', (1,1): '.++', (None,None): '   ',
      (1,0): '.+ ', (0,1): '. +',
      (-1,0):'.- ', (2,0): '.2 ', (-2,0): '-2 '}
def biSquareTri(num1, num2, n):
    return ''.join([''.join([dd[triCo(num1, x, y),triCo(num2, x, y)]
                             for x in range(n)])
                    +'\n'
                    for y in range(n)])

def squareItFromTri (line):
    numbers = map(int, line.split())
    beta, numbers = numbers[0], numbers[1:]
    return squareTri(numbers), beta

def squareTri2 (line):
    numbers = map(int, line.split())
    beta, numbers = numbers[0], numbers[1:]
    n = len (numbers)
    s = biSquareTri(numbers[:n/2], numbers[n/2:], triRoot(n/2))
    return s, beta
