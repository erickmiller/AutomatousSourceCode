import math
testcase=int(input())
def isSquare(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False
for i in range(1,testcase+1):
  n=int(input())
  n1=5*n*n-4
  n2=5*n*n+4
  if((isSquare(n1))or(isSquare(n2))):
    print("IsFibo")
  else:
    print("IsNotFibo")