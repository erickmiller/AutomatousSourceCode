def mySqrt():
    n=int(input("O hai, please enter a number you'd like to take square root of it:"))
    if n>0:
	    approximation = 0.5 * n
	    b = 0.5 * (approximation + n/approximation)
	    while b != approximation:
             approximation = b
             b = 0.5 * (approximation + n/approximation)
    else: 
        print("please enter a nonzero value")
    return approximation
def main():
    print(mySqrt())
main()
