#48) Given a integer, write code to check if it's a square of some integer, can't use sqrt()
def squareRootUsingBinarySearch(num):
	low = 0 
	high = num
	while (low<=high):
		mid = (low+high) / 2
		square = mid ** 2
		if square == num :
			return True
		elif square < num :
			low = mid + 1
		elif square > num:
			high = mid - 1
	return False


def main():
	num = input("Enter the number")
	if squareRootUsingBinarySearch(num) :
		print "%s is a perfect square"%num
	else:
		print "%s is not a perfect square"%num

main()