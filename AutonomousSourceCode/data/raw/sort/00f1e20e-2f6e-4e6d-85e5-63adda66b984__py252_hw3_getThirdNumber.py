import random

def getThird(*nums):
	after_sort = sorted(nums,reverse = True)
	print ('After sorting:',after_sort)
	return after_sort[2]

print (getThird(10,5,99,1000,22,3,2,900,1,8))


