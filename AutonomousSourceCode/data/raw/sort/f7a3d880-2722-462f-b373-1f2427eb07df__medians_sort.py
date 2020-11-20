pairs_A = [int(s) for s in open("Median.txt").read().rstrip().split()]
l = [1, 2, 3, 4, 5]

def medians(array):
	m_k = 0 
	sorted_list = []
	medians = []
	for element in array:
		sorted_list.append(element)
		sorted_list.sort()
		print len(sorted_list)
		if len(sorted_list)%2 == 0:
			m_k = sorted_list[len(sorted_list)/2-1]
		elif len(sorted_list) == 1:
			m_k = sorted_list[0]
		elif len(sorted_list)%2 == 1:
			#print (len(sorted_list)+1)/2
			m_k = sorted_list[(len(sorted_list)+1)/2-1]
		else:
			return "error"
		print "m_k = " , m_k , "\n"
		medians.append(m_k)
	return sum(medians)%10000

print "sum"
print medians(pairs_A)