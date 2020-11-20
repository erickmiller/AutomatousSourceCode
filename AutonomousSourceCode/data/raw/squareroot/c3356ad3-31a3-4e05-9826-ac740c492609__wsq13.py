def sqrt(a):
    if a==0:
        return a
    elif a<0:
        return ('Error: The square root of a negative number is an imaginary number')
    else:
        n=0
        i=0
        while n<a:
            n=i**2
            i=i+1

        if n==a:
            return (i-1)

        else:
            g=(i-1)
            ng=((a/g)+g)/2
            while (ng != g):
                g=ng
                ng=((a/g)+g)/2
            return ng

r='y'
while r=='y' or r=='Y':
    while True:
        try:
            x=float(input('Please enter a number to apply square root: '))
            break
        except ValueError:
            print ('This is not a number, please try again')

    print (sqrt(x))
    r=input('Do you want to try any other number?(y/n) ')
