#8.8.py
#Calculating the Square Root of a Number using Newton-Raphson Method 


#Function to return absolute value
def absoluteValue(x):        
        if(x<0):
           x=-x
        return x

#function to calculate square root
def squareRoot(x):
        epsilon=0.0001
        guess=1.0
        while(absoluteValue(guess*guess-x)>=epsilon):
                guess=(x/guess+guess)/2.0
        return guess

#Main()
def main():
        print("squareRoot (2.0) = {0}".format(squareRoot (2.0)));
        print("squareRoot (144.0) = {0}".format(squareRoot (144.0)));
        print("squareRoot (17.5) = {0}".format(squareRoot (17.5)));

#Setting top level conditional script
if __name__=='__main__':
        main()


