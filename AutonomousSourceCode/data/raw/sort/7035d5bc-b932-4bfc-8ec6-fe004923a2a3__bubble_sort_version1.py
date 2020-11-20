def bubble_sort(mylist):
	length=len(mylist)
	for i in range(length-1):
		if (mylist[i]>mylist[i+1]):
			temp=mylist[i]
			temp2=mylist[i+1]
			mylist[i]=temp2
			mylist[i+1]=temp
			bubble_sort(mylist)

	return mylist

print (bubble_sort([5,19,4,1,36,99,2]))

assert bubble_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
assert bubble_sort(["Greg", "Armen", "Ken"]) == sorted(["Greg", "Armen", "Ken"])
