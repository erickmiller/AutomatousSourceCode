# Michael Coomey - Lab #2

Answers = """


"""

def GetANumber (PromptMessage):
    Num = -1
    while (Num < 1):
        Num = requestNumber(PromptMessage)
        if (Num <1):
            showError("Input can not be negative!")
    return Num

def Process (N):
    print "The Number is " + str(N)
    print "The Square is " + str(N)
    print "The Square root is " + str(math.sqrt(N))
    return

def Run():
    Process(GetANumber("Please enter a positive number, " + requestString("Enter your name")))
    return 