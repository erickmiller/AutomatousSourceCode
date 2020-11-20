import sys

def main():
	a = [1, 20, 55,10,15]
	b = []
	b = middle(a)
	print 'Old : ', a
	print 'New :', b
	c =[]
	a.sort()
	print 'Old Sorted : ',a
	print 'New Sorted : ',middle(a)

def middle(a):
	b = []
	b = a[1:4]
	return b

if __name__=='__main__':
	main()

