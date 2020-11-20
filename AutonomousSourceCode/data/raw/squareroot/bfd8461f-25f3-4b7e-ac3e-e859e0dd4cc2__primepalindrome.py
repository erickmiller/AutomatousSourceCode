#Write a program to determine the biggest prime palindrome under 1000. 

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

def is_palindrome(num):
    dummy = int(num)
    rev = 0
    while(dummy!=0):
        r = dummy%10
        rev = rev*10+r
        dummy=int(dummy/10)
    if(num==rev):
            return 0
    return 1    


counter = 0
for i in range(1000,1,-1):
    if(is_prime(i)==0 and is_palindrome(i)==0):
        print(i)
        break
    