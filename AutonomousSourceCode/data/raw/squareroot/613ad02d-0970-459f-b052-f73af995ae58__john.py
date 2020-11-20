def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def isfib(n):
  sq = 5*(n*n)+4

	if isqrt(sq)**2-sq==0:
		return True
	else:
		sq = sq-8 
		if isqrt(sq)**2-sq==0:
			return True
		else:
			return False
