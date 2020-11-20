from random import randrange
import sorting

def populate_random_data():
	data_limit = randrange(25, 50)
	data = [randrange(0, 999) for i in xrange(data_limit)] 
	return data

'''
	Test bubble sort
'''
def test_bubble_sort():
	data = populate_random_data()
	sorting.bubble_sort(data)

	assert sorted(data) == data


'''
	Test insertion sort
'''
def test_insertion_sort():
	data = populate_random_data()
	sorting.insertion_sort(data)

	assert sorted(data) == data

'''
	Test merge sort
'''
def test_merge_sort():
	data = populate_random_data()
	sorting.merge_sort(data)

	assert sorted(data) == data

'''
	Test selection sort
'''
def test_insertion_sort():
	data = populate_random_data()
	sorting.selection_sort(data)

	assert sorted(data) == data