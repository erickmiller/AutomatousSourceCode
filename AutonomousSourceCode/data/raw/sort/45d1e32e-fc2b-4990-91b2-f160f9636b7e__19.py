def sortTuples():
	result = []
	while(True):
		input = raw_input()
		if (input == ""):
			break;
		else:
			items = tuple(input.split(","))
			result.append(items)
	return sorted(result, key = lambda x:(x[0], x[1], x[2]))

			


print sortTuples()