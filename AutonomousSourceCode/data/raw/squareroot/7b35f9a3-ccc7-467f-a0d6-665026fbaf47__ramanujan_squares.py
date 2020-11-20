import sys
#import ipdb

def get_ramanujan_squares():
    
    cx = 1
    cy = 1
    
    while True:
        d = abs((cx - cy) // 2)
        
        x = (cx + cy) // 2 if d % 2 == 0 else d
        y = abs((7 * cx - cy) // 2) if d % 2 == 0 else (7 * cx + cy) // 2
        
        cx = x
        cy = y
        
        yield [cx, cy]
        
def pow_seven(n):
    
    p = 0
    d = n
    
    while d % 7 == 0:
        d //= 7
        p += 1
    
    if p > 0:
        t, e = is_root(d, 2 * p + 1)
        
        if t:
            return [True, p, e]
    
    return [False, None, None]
    
def is_root(n, p):
        
    r = get_root(n, p)

    return [r**p == n, r]

def get_root(n, p):
    
    sj, ej = find_search_range(n, p)
    
    return root_binary_search(sj, ej, n, p)

def find_search_range(n, p):

    l = 1
    
    #establish limits of search for binary search for root(n)
    while (l**p < n):
        l *= 2
        
    s = l // 2
    e = l

    return [s, e]

#returns smallest integer whose square is greater than or equal to n
def root_binary_search(s, e, n, p):
    
    while (s <= e):
        m = (s + e) // 2
        
        if (m**p < n):
            s = m + 1
        elif (m**p > n):
            e = m - 1
        else:
            return m
    
    return s - 1
        

def get_all_ram_squares(all=False, nn=50):
    
    r = get_ramanujan_squares()
    x, y = r.__next__()
    
    c = to_n(start=3, end=nn, inf=all)
    
    for i in c:
        try:
            #print(i, ':', x, ',', y)
            
            x, y = r.__next__()
            
            t, p, e = pow_seven(x)
            
            if t:
                print("\t!!!!", x, ':', p, ',', e, "!!!!")
            
            #print(i, ':', x, ',', y, ',', e)
        except KeyboardInterrupt:
            print('\n' + str(i), ':', x, ',', y)
            
            sys.exit(0)
    
def to_n(start=0, end=0, inf=False):
    
    x = start
    
    while inf or x < end:
        yield x
        x += 1