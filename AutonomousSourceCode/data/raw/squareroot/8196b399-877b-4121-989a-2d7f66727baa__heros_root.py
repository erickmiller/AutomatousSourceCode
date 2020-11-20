def int_rac(n, guess):
    """Integer Square Root of an Integer"""
    x = [guess]
    
    while (x[-1]+n/x[-1])/2 != x[-1]:
        x.append((x[-1]+n/x[-1])/2)
        
    return len(x)