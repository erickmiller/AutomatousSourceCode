'''
Square root convergents

answer: 153
'''

def expansion(x):
	m = 2
	n = 1
	for i in xrange(0, x):
		m, n = n+2*m, m
	m, n = m+n, m
	return m, n


def solution():
	count = 0
	for i in xrange(0, 999):
		m, n = expansion(i)
		if len(str(m)) > len(str(n)):
			count += 1
	return count


if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
