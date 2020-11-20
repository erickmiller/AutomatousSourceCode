# Newton's method to approximate square root
def sqrt(w, eps = 1.e-14, maxIter = 100):
  x = 1.
  for i in range(maxIter):
    x_old = x
    x = (x + w/x)/2
    if abs(x - x_old)/w < eps:
      return x




def fsolve(func, x0):
  pass

print(sqrt(99))