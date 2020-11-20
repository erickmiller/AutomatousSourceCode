class A:
    def __init__ (self, haha, c):
        self.haha = haha
        self.c = c

    def __str__ (self):
        return str(self.haha) + self.c

    def __lt__ (self, other):
    	return self.haha < other.haha

a = A(2, 'a')
b = A(5, 'b')
c = A(7, 'c')
d = A(5, 'd')
M = [a,d,c,b]
M.sort()
# N = sorted(M, key = lambda hehe: hehe.haha)
for n in M:
	print n