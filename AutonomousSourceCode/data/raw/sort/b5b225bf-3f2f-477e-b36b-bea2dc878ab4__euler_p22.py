def sort_names(list_of_names):
	name_tuples = [(ord(name[0]), name.lower()) for name in list_of_names]
	sorted_name_tuples = sorted(name_tuples)
	sorted_names = [name for value, name in sorted_name_tuples]
	return sorted_names


def get_alph_score(name):
	if name == "":
		return 0
	return (1 + ord(name[0]) - ord("a")) + get_alph_score(name[1:])

def iterate_over_names(name_list):
	sorted_names = sort_names(name_list)
	name_and_position_tupels = [(index + 1) * get_alph_score(name) for index, name in enumerate(sorted_names)]

	return sum(name_and_position_tupels)

if __name__ == "__main__":
	with open ("p22_names.txt", "r") as name_file:
		name_list = name_file.read().replace('"', '').split(',')
		print iterate_over_names(name_list)
