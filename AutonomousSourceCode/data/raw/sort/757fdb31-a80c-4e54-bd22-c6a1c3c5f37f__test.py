def groupAnagrams(strs):
        result=[]
        d={}
        while strs:
            word=strs.pop()
	    print sorted(word)
            if d.has_key(sorted(word)):
                d[sorted(word)]=d[sorted(word)].append(word)
            else:
                d[sorted(word)]=[word]
        for item in d.values():
            if len(item)>1:
                item.sort()
	return d.values()

strs=["and","dan"]
print strs
print groupAnagrams(strs)
