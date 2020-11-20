#
# Problem 188
#
#
global basex

basex=1777

def mod_mult(x, y, mod):
    return (x * y) % mod
 
def mod_exp(x, y, mod):
    if y == 0:
        return 1
    print "*"
    root = mod_exp(x, y/2, mod)
    print "%"
    square = mod_mult(root, root, mod)
    print "root root mod", root, mod
    if y % 2 == 0:
        return square
    else:
        return mod_mult(x, square, mod)
 
DIGITS = 8
MOD = 10 ** DIGITS
 
a = 1777
ak = a
for k in range(2, 1856):
    aj = ak
    ak = mod_exp(a, ak, MOD)
    if aj == ak:
        print k, aj
        break


