def subsets(s):
        s.sort()
        r = [[]]
        for e in s:
            r += [x+[e] for x in r]
        return sorted(r)
s = [1,2,3]
mk = [[]]
mk = subsets(s)
for i in mk:
    print i
    
