#! /usr/bin/env python 
from fraction import *
from math import *

def getContinuedFraction(N):
   a = [int(sqrt(N)), int(1.0 / (sqrt(N) - int(sqrt(N))))]
   pnm2 = a[0]             # p[n - 2]
   pnm1 = a[1] * pnm2 + 1  # p[n - 1]
   qnm2 = 1                # q[n - 2]
   qnm1 = a[1]             # q[n - 1]
   Pnm2 = 0                # P[n - 2]
   Pnm1 = a[0]             # P[n - 1]
   Qnm1 = N - a[0] * a[0]  # Q[n - 1]
   n = 2
   while True:
      Pn = a[n - 1] * Qnm1 - Pnm1
      Qn = (N - Pn * Pn) / Qnm1
      a.append(int((a[0] + Pn) / Qn))
      pn = a[n] * pnm1 + pnm2
      qn = a[n] * qnm1 + qnm2
      if a[n] == 2 * a[0]:    # When a[n] == 2a0 we have the term where the continued fraction becomes periodic
         if a[n] == a[n - 1]:
            return a[:2]   # In case it repeats on the second element
         else:
            return a
      pnm2 = pnm1
      pnm1 = pn
      qnm2 = qnm1
      qnm1 = qn
      Pnm1 = Pn
      Qnm1 = Qn
      n = n + 1

if __name__ == "__main__":
   squareRootOfSquareNumber = 2
   sum = 0
   for N in range(2, 10001):
      if N != squareRootOfSquareNumber**2:
         a = getContinuedFraction(N)
         if len(a) % 2 == 0: # If even length, then period is of odd length
            sum += 1
      else:
         squareRootOfSquareNumber += 1

   print 'Answer:', sum
