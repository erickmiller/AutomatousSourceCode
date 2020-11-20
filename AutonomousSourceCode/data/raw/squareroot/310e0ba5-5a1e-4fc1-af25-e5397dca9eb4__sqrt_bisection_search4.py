def squareRoot(x): 
  epsilon = 0.001 
  low = 0
  high = max(x, 1)  
  bisection = (high+low)/2.0

  while abs((bisection**2)-x) >= epsilon and bisection <= x:
    if (bisection**2) > x: 
      high = bisection
    else:
      low = bisection
    bisection = (high+low)/2
  return bisection

print squareRoot(0.5)