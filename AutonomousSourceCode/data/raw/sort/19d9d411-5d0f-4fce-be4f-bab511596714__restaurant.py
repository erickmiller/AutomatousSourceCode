
import sys

def main():
	T = int(sys.stdin.readline().strip())
	while T > 0:
		line = sys.stdin.readline().rstrip('\n')
		sort = sorted(line.strip().split(' '))
		g = gcd(int(sort[1]), int(sort[0]))
		val = (int(sort[0]) * int(sort[1])) / (g * g)
		print val
		T -= 1

def gcd (x, y):
	while y:
		x, y = y, x % y
	return x

if __name__ == '__main__':
	main()
