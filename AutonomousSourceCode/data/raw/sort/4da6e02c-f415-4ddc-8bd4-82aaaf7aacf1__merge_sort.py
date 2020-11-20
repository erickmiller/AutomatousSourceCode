


def merge_sort(someList):
	if len(someList) == 1:
		return someList
	r = someList[:len(someList)/2]
	l = someList[len(someList)/2:]
	sorted_right = merge_sort(r)
	sorted_left = merge_sort(l)
	return merge(sorted_right, sorted_left)

def merge(one, two):
	mySorted = []
	while one != [] or two != []:
		if one == []:
			mySorted += two
			break	
		elif two == []:
			mySorted += one
			break
		if one[0] <= two[0]:
			mySorted += [one[0]]
			one = one[1:]
		else:
			mySorted += [two[0]]
			two = two[1:]
	return mySorted


test1 = range(20)[::-1]
print test1
print merge_sort(test1)
import random
test2 = [random.randint(1,1000) for x in range(10**3)]
print test2

print merge_sort(test2)
