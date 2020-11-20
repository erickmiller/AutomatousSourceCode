def bubble_sort(my_list):
	length=len(my_list)
	not_sorted=True
	times_iter=0
	while (times_iter<length-1):
		times_swap=0
		for i in range(1,length):
			if (my_list[i-1]>my_list[i]):
				times_swap+=1
				temp=my_list[i-1]
				my_list[i-1]=my_list[i]
				my_list[i]=temp

		if (times_swap==0):
			not_sorted=False
			break
		times_iter+=1

	return my_list
    


print (bubble_sort([5,19,31,15,0]))


assert bubble_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
assert bubble_sort(["Greg", "Armen", "Ken"]) == sorted(["Greg", "Armen", "Ken"])
