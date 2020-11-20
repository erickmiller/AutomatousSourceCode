def test(g,s):
    while g*g != s:
        print 'g is {0}'.format(g)
        g = new_g(g,s)
    print 'Found! square root of {0} is {1}'.format(s,g)

def new_g(g,s):
    g = ((g+(s/g))/2)
    return g

def main():
    # g is your best guess for the square root of s
    g = 30000000.00
    s = 25
    test(g,s)

if __name__ =='__main__':main()
