from utils.numbers import rootConvergentGenerator

# Pell's equation

def isSquare(n):
    return int(n**0.5)**2 == n

def diophantineX(d):

    for x, y in rootConvergentGenerator(d, True):
        ans = x**2 - d * y**2
        if ans == 1:
            return x

def challenge066():
    limit = 1000
    solutions = [[d, diophantineX(d)] for d in xrange(1, limit + 1) if not isSquare(d)]
    return max(solutions, key=lambda x: x[1])[0]

answer = 661

if __name__ == "__main__":
    print challenge066()
