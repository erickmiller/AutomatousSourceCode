import math
#def print_n(n):
	#while n > 0:
		#print n;
		#n = n -1;
	#print 'Blastoff!!!'
#print_n(10)

#def test_square_root(a):
	#x=2
	#y = (x + a / x) / 2
	#s = math.sqrt(a)
	
	#while abs(y-s) < 0.0:
		#x = y
	
	#return y ,',', s

#print test_square_root(1)

def eval_loop():
	while True:
		line = raw_input('> ')
		if line == 'done':
			break
		else:
			print eval(line)

eval_loop()



	
		
