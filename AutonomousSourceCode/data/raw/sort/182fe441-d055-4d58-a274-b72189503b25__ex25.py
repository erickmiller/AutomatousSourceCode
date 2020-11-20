def seg_word(sent1):
	list1 = sent1.split(' ')
	return list1
	
def sort_word(list1):
	return sorted(list1)
	
def print_first(list1):
	item1 = list1.pop(0)
	print item1
	
def print_last(list1):
	item1 = list1.pop(-1)
	print item1
	
def sort_sent(sent1):
	list1 = seg_word(sent1)
	return sort_word(list1)
	
def print_first_last(sent1):
	list1 = seg_word(sent1)
	print_first(list1)
	print_last(list1)
	
def print_first_last_sort(sent1):
	list1 = sort_sent(sent1)
	print_first(list1)
	print_last(list1)
	
