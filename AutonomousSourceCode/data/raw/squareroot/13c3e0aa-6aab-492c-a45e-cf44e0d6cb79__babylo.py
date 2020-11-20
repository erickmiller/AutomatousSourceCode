def babylon(root): #Julio Cesar Gonzalez Uribe A01229898
    b=root
    cont=1
    guess=b/2
    if(root==0):
    	return print(root)
    elif(root<0):
    	return print('Error the root can not be negative')
    else:
      while(cont<=3):
        a=root/guess
        ave=(a+guess)/2
        guess=ave
        cont=cont+1
      print (guess) 
num=float(input('give me the number that you want to know his square root: '))
print(babylon(num))        