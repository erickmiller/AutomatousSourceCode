import math

def square_root(a,x):
    for i  in a:
         	y = (x + i/x) / 2
              return y

def math_squrt(a,x):
	for j  in a: 
		m = math.sqrt(j)
 		return m

def test_square_root(a,x):
	for k in a:

		     m = math_squrt(k,x)
    		     y = square_root(k,x)
     		     c = m - y
    		 print a ,'         ',  m ,'                ', y,'          ', c


test_square_root(range(10),3)

