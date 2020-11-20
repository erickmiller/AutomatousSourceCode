#Pablo Enrique Cárdenas Viera
#A01630814
#Function
def Root(n):
    x=n
    y=0
    while(x!= y):
        y=x
        x=(n/x + x)/2
    return x
print("I will calculate the square root af any number you type")
x= float(input("type the number: "))
if(x== 0 ):
    print("The square root is: "+str(x))
elif( x < 0):
    print("Negative numbers can not have square root")
else:
    Answer= Root(x)
    print ("The square root is: "+str(Answer))