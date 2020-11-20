'''
exercise:7.2 Computes the square root of a number using Newtons approximation method

'''

def sqrt(num):
  epsilon = 0.000001
  rt=num/2
  while True:
    newrt=(rt+num/rt)/2
    if abs(newrt-rt) < epsilon :
      return newrt   
    rt=newrt
    
def get_input(prompt):
  num=raw_input(prompt)
  return num
  
def main():
  prompt="enter the number :  "
  num=float(get_input(prompt))
  print "The square root of {0} is : ".format(num),sqrt(num)

if __name__=='__main__':
  print '*'*30,'\n'
  main()
  print '\n','*'*30
