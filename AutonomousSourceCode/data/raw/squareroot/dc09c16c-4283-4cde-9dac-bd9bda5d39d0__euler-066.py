def is_square(n):
    root = int(n**.5)
    return root*root == n

largest = 0
count = 0
for i in xrange(3,1001):
    if is_square(i):continue
    m = 0
    d = 1
    a = int(i**.5)
    s = a
    h0 = a
    k0 = 1
    h_1 = 1
    k_1 = 0
    while h0*h0-i*k0*k0 !=1:
        m = d*a - m
        d = (i-m*m)/d
        a = int((s+m)/d)
        temp_h = h0
        temp_k = k0
        h0 = a*temp_h+h_1
        k0 = a*temp_k+k_1
        h_1 = temp_h
        k_1 = temp_k
    if h0>largest:
        largest = h0
        count = i

print "The answer is :",count
print "The number is :",largest
