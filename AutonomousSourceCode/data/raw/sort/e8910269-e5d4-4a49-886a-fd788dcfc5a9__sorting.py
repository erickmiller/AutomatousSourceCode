import moka

def selection_sort(data):
	if len(data) < 2:
		return data

	min = data[0]
	for i in data:
		if i < min:
			min = i

	data.remove(min)
	sorted_data = selection_sort(data)
	sorted_data.insert(0, min)
	return data

def insertion_sort(data, sorted_data = None):
	if not sorted_data:
		sorted_data = []

	if len(data) == 0:
		return sorted_data

	first = data[0]
	rest = data[1:]

	if len(sorted_data) == 0:
		sorted_data.append(data[0])
		return insertion_sort(rest, sorted_data = [first])

	if first >= sorted_data[-1]:
		sorted_data.append(first)
		return insertion_sort(rest, sorted_data = sorted_data)

	for i in range(len(sorted_data) - 1, -1, -1):
			if first >= sorted_data[i]:
				sorted_data.insert(i + 1, first)
				return insertion_sort(rest, sorted_data = sorted_data)

	sorted_data.insert(0, first)

	return insertion_sort(rest, sorted_data = sorted_data)

def merge_sort(data):
	def merge_arrays(a, b, result = None):
		print a, b, result
		if not result:
			result = []

		if len(a) == 0 and  len(b) == 0:
			return result

		if len(a) > 0 and len(b) > 0:
			if a[0] < b[0]:
				result.append(a[0])
				return merge_arrays(a[1:], b, result)
			if a[0] > b[0]:
				result.append(b[0])
				return merge_arrays(a, b[1:], result)
			result.append(a[0])
			result.append(b[0])
			return merge_arrays(a[1:], b[1:], result)

		if len(a) > 0:
			result.extend(a)
			return result

		result.extend(b)
		return result

	if len(data) < 2:
		return data

	if len(data) == 2:
		if data[1] < data[0]:
			return [data[1], data[0]]
		return data

	mid_point = len(data) / 2

	return merge_arrays(merge_sort(data[0:mid_point]), merge_sort(data[mid_point: len(data)]))


sorts = [selection_sort, insertion_sort, merge_sort]

