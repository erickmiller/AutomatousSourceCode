#!/usr/bin/python -tt

def ThirdGreatest(ary):

	myDict = {}
	
	#words in array are keys in dictionary
	#values in dictionary represents their order in original array
	for i in range(len(ary)):
		myDict[ary[i]] = i

	#sort dictionary by key length
	sortedByLength = sorted(myDict, key=len, reverse=True)

	#sortedByLength is now a list sorted by word length, if lengths are same,
	#then check with the values in dictionary for their original location
	if len(sortedByLength[1]) == len(sortedByLength[2]):
		#2nd and 3rd same length
		if myDict[sortedByLength[1]] > myDict[sortedByLength[2]]:
			return sortedByLength[1]
		else:
			return sortedByLength[2]
	elif len(sortedByLength[2]) == len(sortedByLength[3]):
		if myDict[sortedByLength[2]] > myDict[sortedByLength[3]]:
			return sortedByLength[2]
		else:
			return sortedByLength[3]
	else:
		return sortedByLength[2]

def main():

	result = ThirdGreatest(["hello", "world", "after", "all"] )
	print result

if __name__ == "__main__":
  main()