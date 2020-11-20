# Find the unique positive integer whose square is 1_2_3_4_5_6_7_8_9_0, where each '_'
# is a single digit.

# First observe that this square number is divisible by 10, and since it is necessarily a 
# square, it must also be divisible by 100.  This follows from the fact that if a prime 
# p divides n^2, then so does p^2.  Thus, the last 3 digits of the square must be 900.

# Moreover, one calculates that the square root of 1929394959697989900 is 1389026623.11,
# which tells us that the desired integer must be a multiple of 10 less than 1389026623,
# and the square root of 1020304050607080900 is 1010101010.1, which tells us that the
# desired integer is greater than 1010101010.

# Answer: 1389019170, with 1389019170^2 = 1929374254627488900


def nice_digits(n):
	digits = []
	
	while (n>0):
		digits.append(n%10)
		n=n/10
	digits.reverse()
	
	nice = True
	for i in range(0,9):
		if(digits[2*i]!=i+1):
			nice = False
			break
	return nice


for i in range(101010101,138902663):
	i=10*i
	j=i*i
	if (nice_digits(j)):
		print i
