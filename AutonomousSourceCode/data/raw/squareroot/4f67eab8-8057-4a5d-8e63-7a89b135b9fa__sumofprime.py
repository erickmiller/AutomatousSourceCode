# Write a program to determine the sum of the first 1000 prime numbers. 
def square_root(num):
    initial_guess = 1
    while 1:    
        f_x = float(initial_guess*initial_guess - num)
        der_f_x = float(2 * initial_guess)
        new_guess = initial_guess - (f_x/der_f_x)*1.0
        if( abs(initial_guess-new_guess) < 0.001 or abs(initial_guess-new_guess)==0):
            break
        initial_guess = new_guess
    return "%.4f" %new_guess    
    
def is_prime(num):
    root = int(float(square_root(num)))
    for i in range(2,root+1):
        if( num%i == 0 ):
            return 1
    return 0    

counter = 0
i = 2
sum =0 
while counter < 1000:
    if(is_prime(i)==0):
        sum = sum + i
        counter=counter+1
        #print("counter = %d" %counter)
    i=i +1
    #print("i=%d" %i)
print(sum)