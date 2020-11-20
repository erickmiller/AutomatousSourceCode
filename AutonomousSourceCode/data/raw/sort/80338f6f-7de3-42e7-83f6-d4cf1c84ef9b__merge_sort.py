def merge_sort(a,b):
	"""merge_sort two sorted lists"""
	out = []
	i = 0
	j = 0

	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			out.append(a[i])
			i += 1
		elif b[j] < a[i]:
			out.append(b[j])
			j += 1
		elif a[i] == b[j]:
			out.append(a[i])
			out.append(b[j])
			i += 1
			j += 1

	if i < len(a):
		out.extend(a[i:])
	if j < len(b):
		out.extend(b[j:])

	return out

# lst1 = [0, 2, 5, 7]
# lst2 = [3, 4, 9, 10, 11]

# print merge_sort(lst1, lst2)

def sort_merge_rec(lst):
	"""sort an unsorted list using merge sort. takes in list, returns that list, sorted"""

	if len(lst) > 1:
		left = sort_merge_rec(lst[:len(lst)/2])
		right = sort_merge_rec(lst[len(lst)/2:])
		return merge_sort(left, right)
	else:
		return lst

if __name__=='__main__':
    from timeit import Timer

    t = Timer("sort_merge_rec", "from __main__ import sort_merge_rec")
    print sort_merge_rec([2, 5, 3, 7, 6, 1]) 
    print t.timeit()
	
