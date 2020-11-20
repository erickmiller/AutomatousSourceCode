__author__ = 'Eutimio'
print(" Eutimio MAchuca Parra A01630244")
def raiz(n):
    x=n
    y=0
    while(x!= y):
        y=x
        x=(n/x + x)/2
    return x
print(" this program returns you he square root of a number")
num= float(input("give me a number"))
if(num== 0 ):
    print("The square root is:", num)
elif( num < 0):
    print(" there are not square root for negative numbers")
else:
    sqrt= raiz(num)
    print (" the square root is:", sqrt)

