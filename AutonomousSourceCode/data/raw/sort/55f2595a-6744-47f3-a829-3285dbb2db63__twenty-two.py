def input():
	data=[]
	for line in open("twenty-two.dat"):
		names=line.split(",")
		for name in names:		
			data.append(name.strip('"'))
	return data

def my_sort(list):
        sorted_list=[list[0]]
        for x in list[1:]:
                i=0
                while i<len(sorted_list):
                        if sorted_list[i]>x:
                                break
                        i+=1
                sorted_list=sorted_list[:i]+[x]+sorted_list[i:]
        return sorted_list

def name_num(name):
        s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sum=0
        for i in name:
                sum+=s.find(i)+1
        return sum

def problem_22():
	#not correct
	#summing the letters first just won't work. a+b+c not unique
	data=input()
	new_data=[]
	for name in data:
		new_data.append(name_num(name))
	#sorted=my_sort(new_data)
	sorted_data=sorted(data)
	sum=0
	for i in range(len(sorted_data)):
		sum+=name_num(sorted_data[i])*(i+1)
	return sum

if __name__=="__main__":
	data=sorted(input())
	sum=0
	for name in data:
		sum+=name_num(name)*(data.index(name)+1)
	print sum
	print problem_22()
