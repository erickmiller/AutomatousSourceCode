data = [1,3,9,4,111,150]

def InsertSort(data):
	for j in range(1,(len(data)-1)):
		key = data[j]
		i = j-1
		while(i>=0 and data[i]>key):
			data[i+1] = data[i]
			i = i-1
		data[i+1] = key
	return data

def main():
	print data
	SortedData = InsertSort(data)
	print SortedData

main()

