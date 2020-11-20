list1 = [4,8,16,22,83,9]
list2 = [27,9,1,0,6]
list3 = [6,5,3,1,8,7,2,4]

def bubble_sort(lst):
	is_sorted = False
	while is_sorted == False:
		is_sorted = True
		for index in range(len(lst)-1):
			if lst[index] > lst[index+1]:
				is_sorted = False
				lst[index], lst[index+1] = lst[index+1], lst[index]
	return lst

def optimized_bubble_sort(lst):
	is_sorted = False
	n = len(lst)-1
	while is_sorted == False:
		is_sorted = True
		for index in range(n):
			if lst[index] > lst[index+1]:
				is_sorted = False
				lst[index], lst[index+1] = lst[index+1], lst[index]
		n -= 1
	return lst
 
def merge_sort(lst):
	if len(lst) <= 1:
		return lst
	sorted_list = []
	mid = len(lst)/2
	lst1 = merge_sort(lst[:mid])
	lst2 = merge_sort(lst[mid:])
	while len(lst1) > 0 and len(lst2) > 0:
		if lst1[0] < lst2[0]:
			sorted_list.append(lst1.pop(0))
		else:
			sorted_list.append(lst2.pop(0))
	sorted_list = sorted_list + lst1 + lst2
	return sorted_list

def merge_sort_pointer(lst):
	if len(lst) <= 1:
		return lst
	sorted_list = []
	mid = len(lst)/2
	lst1 = merge_sort_pointer(lst[:mid])
	lst2 = merge_sort_pointer(lst[mid:])
	index1 = 0
	index2 = 0
	while index1 < len(lst1) and index2 < len(lst2):
		if lst1[index1] < lst2[index2]:
			sorted_list.append(lst1[index1])
			index1 += 1
		else:
			sorted_list.append(lst2[index2])
			index2 += 1
	sorted_list = sorted_list + lst1[index1:] + lst2[index2:]
	return sorted_list

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        less = []
    	pivots = []
    	more = []
        pivot = lst[0]
        for num in lst:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
            else:
                pivots.append(num)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivots + more

def quick_sort_inplace(lst):
    _quicksort(lst, 0, len(lst) - 1)
 
def _quicksort(lst, start, stop):
    if stop - start > 0:
        pivot, left, right = lst[start], start, stop
        while left <= right:
            while lst[left] < pivot:
                left += 1
            while lst[right] > pivot:
                right -= 1
            if left <= right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        _quicksort(lst, start, right)
        _quicksort(lst, left, stop)