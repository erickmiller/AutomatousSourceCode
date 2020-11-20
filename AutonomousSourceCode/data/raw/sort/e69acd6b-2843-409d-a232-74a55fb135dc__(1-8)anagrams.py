#!/usr/bin/python

def sortchar(W):
	L = list(W)
	L.sort()
	return ''.join(L)

if __name__ == "__main__":
	wordList = ['abcd','bacd','e','f','rt','tr','zzz','zz','dcab']
	map1 = {}
	output = []
	for w in wordList:
		sorted_w = ''.join(sorted(w)) #or sortchar(w)
		if sorted_w not in map1:
			map1[sorted_w] = [w]
		else:
			map1[sorted_w].append(w)
	for k in map1.keys():
		if len(map1[k])>1:
			output.append(map1[k])
	print output;


