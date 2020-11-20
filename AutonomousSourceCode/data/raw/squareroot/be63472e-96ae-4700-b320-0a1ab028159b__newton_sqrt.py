def newsqrt(a):
    x=a/2
    e=0.0005
    while True:
        y=(x+a/x)/2
        if x==y and abs(y-x)<e:
              return y
              break
        else:
               x=y
n=float(raw_input('enter a\n'))
print "square_root of",n,"is",newsqrt(n)

