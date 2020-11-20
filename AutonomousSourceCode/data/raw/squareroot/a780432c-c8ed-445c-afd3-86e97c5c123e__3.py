def test_square_root():
	for i in range(1,10):
		sr=square_root(float(i))
		msr=math.sqrt(float(i))
		print '%f %f %ff %f %f %f'%(float(i),sr,msr,abs(sr-msr))

def square_root(a):
	x=3
	while True:
		y=(x+a/x)/2
		if abs(x-y)<epsilon:
			break
		x=y

	return x


import math
epsilon=0.0000000000001
test_square_root()
