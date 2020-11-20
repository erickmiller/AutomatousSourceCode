list_to_sort = ['representative','numeric','senile','effluent','ear','bespectacled','elegiac','ex-developer']

def count_e(s):
	return s.count('e')
	
sorted_list = sorted(list_to_sort,key=count_e)

for item in sorted_list[::-1]:
	print item + ' ' + str(count_e(item))
