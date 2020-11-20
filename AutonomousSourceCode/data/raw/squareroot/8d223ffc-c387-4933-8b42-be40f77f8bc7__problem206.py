
alldigits = [1,2,3,4,5,6,7,8,9,0]
subdigits = [alldigits[len(alldigits) - index - 1:] for index in range(len(alldigits))]

def isSquare(a):
    '''isSquare(int) -> int --  Returns the square root of a if a is a square in the positive integers, None otherwise'''
    # If a is a small number, then we can do this quick version
    if 0 <= a <= 2 ** 50:
        sr = int(a ** (1 / 2.0))
        if sr ** 2 == a:
            return sr
    else:
        raise ValueError("get a better function")
    	
def eq(n, upto):
	print(str(n)[::-1])
	l = [int(b) for index,b in enumerate(str(n)[::-1]) if index%2 == 0][::-1]
	m = alldigits[len(alldigits) - upto:]
	print('l', l)
	print('m', m)
	return l == m
	

start = 102030405060708090**(1/2.0) # 319421985.8755939
end = 192939495969798999**(1/2.0) # 439248785

def candidates(endings):
	newendings = []
	for ending in endings:
		upto = (len(str(ending)) - 1)//2 + 1
		start = alldigits[len(alldigits) - upto] * 10**(upto) + ending
		end = start + 9*10**(upto-1)
		step = 10**(upto-1)
		print(start, end, step)
		for a in range(start,end, step):
			print('a', a)
			if isSquare(a):
				newendings.append(a)
		return newendings

print(candidates([0]))
print(candidates([900]))
