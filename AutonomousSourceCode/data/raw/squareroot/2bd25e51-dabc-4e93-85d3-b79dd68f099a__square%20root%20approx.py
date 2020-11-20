def square_root(a):
    x = a/(2.0**(len(str(a))))
    
    while True:
        y = (x + (a/x))/2.0
        if abs(y-x)<=0.0000001:
            
            break
        else:
            x = y
            print x
        return x
        
    
