# /usr/bin/python
#coding: utf-8
__author__ = 'xujw'

def less(v,w):
	return v < w

def exch(a,i,j):
	t = a[i]
	a[i] = a[j]
	a[j] = t

def sort(a):
	for i in range(0,len(a)):
		#将a[i]和a[i+1...n]中最小的元素交换
		min = i
		for j in range(i+1,len(a)):
			if less(a[j],a[min]):
				min = j
		exch(a,i,min)

def show(a):
	print(a)

def isSorted(a):
	for i in range(1,len(a)):
		if less(a[i],a[i-1]):
			return False
	return True

if __name__ == "__main__":
	a = [6,2,8,1,9]
	print isSorted(a)
	sort(a)
	show(a)
	print isSorted(a)