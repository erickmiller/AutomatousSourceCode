#euler 206
"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
#in order for last digit of square to be 0, second to last digit must also be 0
#so square root must be multiple of 10
#consider 1_2_3_4_5_6_7_8_9 and multiply answer by 10

def found(n):
    n_string = str(n)
    for i in range(9):
        if int(n_string[i * 2]) != (i + 1):
            return False
    return True

    
#square root of 10203040506070809 (min) is 101010102
#for square to end in 9, square root must end in 3 or 7
n = 101010103

while not found(n ** 2):
    #increment end 3 to end 7
    if str(n)[-1] == "3":
        n += 4
    #increment end 7 to end 3
    else:
        n += 6

#multiplying by 10
print(n * 10)
