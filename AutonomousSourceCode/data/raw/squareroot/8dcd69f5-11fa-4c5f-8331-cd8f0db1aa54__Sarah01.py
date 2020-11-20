def Adder(N1,N2):
    MyResult = N1 + N2
    return MyResult

def Subtractor(N1,N2):
    MyResult = N1 - N2
    return MyResult
    
def Main():
    X = input("Enter a value for X ---")
    Y = input("Enter a value for Y ---")
    if (X >= Y):
        print "Subtraction happened"
        MyResult = Subtractor(X,Y)
    else:
        print "Addition happened"
        MyResult = Adder(X,Y)
    Result1 = math.sqrt(MyResult)
    print "the square root of ", MyResult, " is ", Result1
    return
    
def Frog():
    print "Yay!"
    return

