import sys 
def cn(s):
	s=int (s)
	i=1
	while (1):
		if i*i==s:
			return i
		elif i*i>s:
			return "no square root"
		else :
			i=i+1			

sqr=sys.argv[1]
print(cn (sqr))
