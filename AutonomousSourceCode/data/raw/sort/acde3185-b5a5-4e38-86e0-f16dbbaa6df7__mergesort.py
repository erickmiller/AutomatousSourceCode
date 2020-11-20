
def main():
	ls = [24,12,2,37,48,28,26,421,585,352,8]
	sorted_ls = mergeSort(ls)
	print("List started as:")
	print(ls)
	print("Sort list looks like:")
	print(sorted_ls)


def mergeSort(a):
	if (len(a) == 1):
		return a

	mid = len(a) // 2
	left = a[0:mid]
	right = a[mid:]

	left = mergeSort(left)
	right = mergeSort(right)

	return merge(left,right)

def merge(a,b):
	c = []

	while (a and b):
		if (a[0] > b[0]):
			c.append(b[0])
			b.pop(0)
		else:
			c.append(a[0])
			a.pop(0)

	while (a):
		c.append(a[0])
		a.pop(0)

	while(b):
		c.append(b[0])
		b.pop(0)

	return c

main()
