def ex_sort(x):
	
	
	y = sorted(x, key= lambda x:x.split('.')[1])
	return y


print ex_sort(['a.py','b.c','v.txt','as.a'])
