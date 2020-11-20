import threading
import _thread
import time
import math
import random


#Square Root Calculator
def mySqrt():
    print()
    print ('***Square Root Calculator***')
    print()
    print ('Please enter your number of choice:')

    x = int (input())

    time.sleep(2)
    
    """Returns the square root of x if x is a perfect square.
Prints an error message and returns none if otherwise."""
    ans = 0
    if x>=0:
        while ans*ans <x:
            ans = ans + 1
        if ans*ans == x:
            print(x, 'is a perfect square.')


            y = math.sqrt(x)
            a = (y, 'is the square root of' , x)
            print (a)

            f = open('sqrt.txt','w+')
            f.write(a)
            f.close()
            
            return ans
        
        else:
            print(x, 'is not a perfect square.')
            return None    
    else: 
            print(x, 'is a negative number.')
            
mySqrt()




#BMI Calculator
def BMI():
    print()
    print("***Body Mass Index(BMI) Calculator***")
    print()
    print("Please fill out the following:")
    print()
    x = eval(input("Your weight in Kilograms: "))
    y = eval(input("Your Height in Meters: "))

    '''BMI formula is mass(Kg) /(Height(m))* (Height(m))'''
    x = float(x)
    y = float(y)

    slp = random.randint(5,7)
    
    print('sleep time chosen is', slp , 'seconds')
    time.sleep(slp)

    c = (((x)/(y*y)))

    print (c , 'is your BMI')
    print()

    print('BMI CHART')
    print ('Below 18.5 = Underweight')
    print ('Between 18.5 and 24.9 = Normal')
    print ('Between 25 and 29.9 = Overweight')
    print ('Above 30.0 = Obese')
    
BMI()

m = random.randint(1,8)
print ()
print('integer generated is ',m)


if m % 2 == 0:
    print('--BMI calculator chosen:: The integer is even')
    _thread.start_new_thread(BMI, ())
else:
    print('Square root calculator chosen:: The integer is odd')
    _thread.start_new_thread(mySqrt, ())

