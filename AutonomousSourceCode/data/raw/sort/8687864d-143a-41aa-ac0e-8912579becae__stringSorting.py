def string_length_sort(strings):
	items_counted = {}
	for item in strings:
	    items_counted.setdefault(item, len(item))
	    
	sorted_by_count = sorted([(value, key) for (key,value) in items_counted.items()])
	return [i[1] for i in sorted_by_count]