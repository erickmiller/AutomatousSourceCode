from nth_root import *

def sum_digs(n):
    s = 0
    while n > 0:
        s += n % 10
        n /= 10
    return s

s = 0
for n in xrange(2,101):
    if (n**.5) == int(n**.5):
        continue
    s += sum_digs(nth_root(n*(10**198),2))
print s

#def square_root_digs_sum(radicand, n, B):
#    x,y,r = 0,0,0
#    temp = radicand
#    digs = 0
#    while temp > 0:
#        digs += 1
#        temp /= 10
#    for i in xrange(0,100):
#        if (i*(n+1)) > digs:
#            a = 0
#        else:
#            a = (radicand / (10**(digs-(n*(i+1))))) % (10**n)
#        x_p = (B**n)*x + a
#        beta = 0
#        while (B * y + beta)**n <= (B ** n) * x + a:
#            beta += 1
#        beta -= 1
#        y_p = B * y + beta
#        r_p = (B ** n) * x + a - ((B * y + beta)**n)
        
        

    # if iterations*n > digs, automatically set a = 0
