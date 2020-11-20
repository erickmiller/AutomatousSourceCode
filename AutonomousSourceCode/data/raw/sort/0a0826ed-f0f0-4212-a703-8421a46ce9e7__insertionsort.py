# sorts a list via insertion sort
def f(x):
 if len(x)==1: return x;
 for a in range(2,len(x)+1):
  i = a-1
  key = x[i]
  while i>0 and x[i-1] > key:
   x[i] = x[i-1]
   i-=1
  x[i] = key
  #x[0,i-1] is sorted
 return x;
