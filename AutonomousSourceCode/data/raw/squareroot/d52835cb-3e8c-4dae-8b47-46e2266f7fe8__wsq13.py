# Aram Rodrigo Curiel Graxiola
# A01229982
# WSQ13

def sqrt(n):
    a = n
    b = 0
    while(b != a):
        b = a
        a = (n/a + a)/2
    return a

print ("This program works giving the square root for each number")

ans = "Yes"
while (ans == "Yes"):
    num = float(input("Give me a number: "))
    if (num == 0):
        print("The square root is: 0")
    elif(num < 0):
        print("There is no square root for negative numbers!!")
    else:
            square = sqrt(num)
            print("The square root is: ",square)
    ans = str(input("Do you want to try again? (Yes/No): "))
    print("Thanks and have a nice day!")
