#2014-09-26
#author: Dean
#some sort implementation in Python 
#include:
#	insertion sort
#	merge sort
def insertionSort(a):
	for i in range(1,len(a)):
		j=i
		newValue=a[j]
		while j>0 and a[j-1]>newValue:
			a[j]=a[j-1]
			j-=1
		a[j]=newValue
	return a  

def mergeSort(a):
	if len(a)==1:
		return a
	else:
		a1=mergeSort(a[:len(a)/2])
		a2=mergeSort(a[len(a)/2:])
		# print 'left',a1
		# print 'right',a2
		return merge(a1,a2)

def merge(a1,a2):
	idx1,idx2=0,0
	a_sorted=[]
	while idx1<len(a1) and idx2<len(a2):
		if a1[idx1]<a2[idx2]:
			a_sorted.append(a1[idx1])
			idx1+=1
		else:
			a_sorted.append(a2[idx2])
			idx2+=1
	if idx1<len(a1):
		a_sorted.extend(a1[idx1:])
	else:
		a_sorted.extend(a2[idx2:])
	# print a_sorted
	return a_sorted

if __name__=="__main__":
	a=[9,8,7,6,5,4,3]
	print 'a',a
	aSort=insertionSort(a)	
	print 'a insertSorted:',aSort
	b=[9,8,7,6,5,4,3,2]
	bMerge=mergeSort(b)
	print 'b:',b
	print 'b MergeSorted:',bMerge

	

	