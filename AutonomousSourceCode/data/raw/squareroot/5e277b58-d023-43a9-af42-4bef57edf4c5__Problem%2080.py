def square_root(n,d = 100):
    nstr = str(n)
    if len(nstr) % 2 == 1: nstr = '0' + nstr
        
    vals = [int(nstr[i:i+2]) for i in range(0, len(nstr), 2)]
    ans = [-1 for i in range(d)]

    p = 0
    r = 0
    vcnt = 0
    vmax = len(vals)
    for i in range(d):
        if vcnt < vmax:
            c = 100*r + vals[vcnt]
            vcnt += 1
        else: c = 100*r
        x = get_max_x(p,c)
        y = x*(20*p + x)
        r = c - y
        p = 10*p + x
        ans[i] = x
    dec = len(vals)
    ans = ans[:dec] + ["."] + ans[dec:]
    return(ans)
def get_max_x(p,c):
    for x in range(1,10):
        if x*(20*p + x) > c:
            break
    return(x-1)
def get_sum(n):
    start = n.index(".") + 1
    return(sum(n[start:]))
    
square_root(2,100)
    