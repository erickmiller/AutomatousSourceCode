
def isFair(s):
    """ determine if n is a palindrome """
    if len(s) <= 1:
         return True
    else:
        return s[0] == s[-1] and isFair(s[1:-1])

def isFair2(s):
    return s == s [::-1]

        
def isSquare(n, listFairs):
    #print "In isSquare"
    for i in listFairs:
        #print n,i
        if n[0] == i[1]:
            return i[0]
    return 0

def isSquare2(n, listFairs):
    
    return 0

def initFairs(n):
    """ initialize an array of fairs up to our end point """
    print "In init fairs with n = " + str(n)
    fairList = []
    for i in xrange(1, n+1):
        if isFair(str(i)): 
            fairList.append((i, i*i))
    return fairList

        
#f = open("C-small-attempt0.in.txt", "r")
#f = open("C-large-1.in.txt", "r")
f = open("test_large.txt", "r")
numTest=f.readline()
#print numTest
case = 1
for line in f:
    line.rsplit()
    fairAndSquareCount = 0
    x, y = line.split(" ")
    x = int(x)
    y = int(y)
    fairs = initFairs(y)
    print len(fairs)
    for z in fairs:
       if z[0] < x :
            continue
       #print str(z) + " is fair"
       #fairs.append(z)
       root = isSquare(z, fairs)
       if root != 0:
          #print "Found fair and square: " + str(root)
          fairAndSquareCount += 1
    #   z += 1
    print "Case #" + str(case) + ": " + str(fairAndSquareCount)
    case +=1    
             
      
   
