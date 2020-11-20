'''Program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
23 April 2014
Luke Barker'''

vectorA =input('Enter vector A: \n').split(' ')
vectorB =input('Enter vector B: \n').split(' ')

def addvectors(a,b):
    iteration = 0    #create variable called iteration
    new_list = []    #create list
    for i in a:
        add = eval(i)+eval(b[iteration])   #adding vector a to b
        new_list.append(add)
        iteration += 1
    return new_list
        
print('A+B =', addvectors(vectorA,vectorB))
       
def productvectors(a,b):
    iteration = 0    #create variable called iteration
    product = 0    #create variable product
    for i in a:
        multiply = eval(i)*eval(b[iteration])   #times vector a to b
        product += multiply
        iteration += 1
    return product

print('A.B =', productvectors(vectorA,vectorB))

def normA(a):
    sum_squares = 0    #create variable for the sum of the squared numbers
    for i in a:
        squares = eval(i)**2   #square number
        sum_squares += squares      
    x = sum_squares**0.5     #square root sum of the squares
    
    return x

print('|A| =', "{0:4.2f}".format(normA(vectorA)))

def normB(b):
    sum_squares = 0    #create variable for the sum of the squared numbers
    for i in b:
        squares = eval(i)**2   #square number
        sum_squares += squares      
    x = sum_squares**0.5   #square root sum of the squares
    
    return x

print('|B| =', "{0:4.2f}".format(normA(vectorB)))
