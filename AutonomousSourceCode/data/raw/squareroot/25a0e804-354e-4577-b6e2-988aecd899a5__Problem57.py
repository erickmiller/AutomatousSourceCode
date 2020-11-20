from fractions import Fraction

class Problem57:
    def getSquareRootIteration(self, iterations):
        if iterations == 1:
            return Fraction(3,2)
        n = 2
        for _ in range(1, iterations):
            n = 2 + Fraction(1, n)
        return 1 + Fraction(1, n)
        
    def answer(self):
        bigNumSum = 0
        for i in range(1, 1001):
            print("iteration:" + str(i))
            frac = self.getSquareRootIteration(i)
            if len(str(frac.numerator)) > len(str(frac.denominator)):
                bigNumSum += 1
        return bigNumSum