from thread import start_new_thread

def square_thread():
	print("calculate the square root of a")
	eps = 0.0000001
	old = 1
	new = 1

	while True:
		old,new = new,(new + a/new) / 2.0
		print old,new
		if abs(new - old) < eps:
			break:
	return new

start_new_thread(square_thread,(99,))
start_new_thread(square_thread,(999,))
start_new_thread(square_thread,(16,))
start_new_thread(square_thread,(81,))

c = raw_input("Type something to quit")
