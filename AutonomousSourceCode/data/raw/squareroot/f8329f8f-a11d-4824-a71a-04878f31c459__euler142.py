def is_square(n):
	if n < 1: return False
	root = int(n**0.5)
	return root*root == n

def euler142():
	squares = [1]
	root = 2

	while True:
		square = root * root
		squares.append(square)

		for iy in range(len(squares)-1):
			y = square - squares[iy]
			if y % 2 != 0: continue
			y = y / 2

			x = square - y
			for iz in range(iy+1, len(squares)-1):
				if squares[iz] >= x: break

				z = x-squares[iz]
				if not is_square(x + z): continue
				if(is_square(y + z) and is_square(y - z)):
					return x + y + z

		root += 1

if __name__ == "__main__":
	print euler142()