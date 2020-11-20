
def merge_sort(a):
	if len(a)==1:
		return a
	mid=int(len(a)/2)
	sortedLeft=merge_sort(a[:mid])
	sortedRight=merge_sort(a[mid:])
	return merge(sortedLeft,sortedRight)

def merge(a,b):
	sz=len(a)+len(b)
	i=0
	j=0
	res=[]
	for k in xrange(sz):
		if a[i]<=b[j]:
			res.append(a[i])
			i+=1
			if i >= len(a):
				res+=b[j:]
				break
		else:
			res.append(b[j])
			j+=1
			if j >= len(b):
				res+=a[i:]				
				break
	return res

if __name__=='__main__':
	import random
	print merge([1,2,3,4,5,6,7,9],[1.5,2,4,8])
	v=[random.random() for i in range(1000001)]
	s=merge_sort(v)
	print "done ", len(s)