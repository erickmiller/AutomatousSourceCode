
def actual_number_wrapper(func):
	def inner_func(number_list):
		actual_numbers = [number_str[len(number_str)-10:len(number_str)] for number_str in number_list]
		sorted_numbers = func(actual_numbers)
		return ["+91 " + n[0:5] + " " + n[5:10] for n in sorted_numbers]
	return inner_func


@actual_number_wrapper
def sort(numbers):
	sorted_numbers = sorted(numbers)
	return sorted_numbers


number_list = []
for x in range(0,input()):
	number_list.append(raw_input())

for n in sort(number_list):
	print n