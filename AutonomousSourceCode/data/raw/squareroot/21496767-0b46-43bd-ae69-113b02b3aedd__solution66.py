#! /usr/bin/env python 
from fraction import *
from math import *

def solvePellEquation(D):
   x = -1
   y = -1
   a = [int(sqrt(D)), int(1.0 / (sqrt(D) - int(sqrt(D))))]
   pnm2 = a[0]             # p[n - 2]
   pnm1 = a[1] * pnm2 + 1  # p[n - 1]
   qnm2 = 1                # q[n - 2]
   qnm1 = a[1]             # q[n - 1]
   Pnm2 = 0                # P[n - 2]
   Pnm1 = a[0]             # P[n - 1]
   Qnm1 = D - a[0] * a[0]  # Q[n - 1]
   n = 2
   found = False
   while not found:
      Pn = a[n - 1] * Qnm1 - Pnm1
      Qn = (D - Pn * Pn) / Qnm1
      a.append(int((a[0] + Pn) / Qn))
      pn = a[n] * pnm1 + pnm2
      qn = a[n] * qnm1 + qnm2
      if a[n] == 2 * a[0]:    # When a[n] == 2a0 we have the term where the continued fraction becomes periodic
         if (n - 1) % 2 != 0: # n - 1 odd -> return (p[n - 1], q[n - 1])
            x = pnm1
            y = qnm1
         else:                # n - 1 even -> return (p[2n - 1], q[2n - 1])
            pnm2 = pnm1
            pnm1 = pn
            qnm2 = qnm1
            qnm1 = qn
            Pnm1 = Pn
            Qnm1 = Qn
            limit = 2 * n - 1 # Want to return p and q at point 2n - 1
            while n < limit:
               n = n + 1
               Pn = a[n - 1] * Qnm1 - Pnm1
               Qn = (D - Pn * Pn) / Qnm1
               a.append(int((a[0] + Pn) / Qn))
               pn = a[n] * pnm1 + pnm2
               qn = a[n] * qnm1 + qnm2
               pnm2 = pnm1
               pnm1 = pn
               qnm2 = qnm1
               qnm1 = qn
               Pnm1 = Pn
               Qnm1 = Qn
            x = pn
            y = qn
         found = True
      pnm2 = pnm1
      pnm1 = pn
      qnm2 = qnm1
      qnm1 = qn
      Pnm1 = Pn
      Qnm1 = Qn
      n = n + 1
   return x, y

if __name__ == "__main__":
   squareRootOfSquareNumber = 2
   largestD = -1
   largestX = -1
   for D in range(2, 1000):
      if D != (squareRootOfSquareNumber * squareRootOfSquareNumber):
         x, y = solvePellEquation(D)
         if x > largestX:
            largestX = x
            largestD = D
      else:
         squareRootOfSquareNumber = squareRootOfSquareNumber + 1

   print 'Answer: D =', largestD, 'and x =', largestX
