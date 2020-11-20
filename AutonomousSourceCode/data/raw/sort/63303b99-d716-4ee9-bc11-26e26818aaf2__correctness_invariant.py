def is_sorted(l):
    if len(l) == 1:
        return True
    for i in xrange(1,len(l)):
        if l[i]<l[i-1]:
            return False
    return True


def insertion_sort(l):
    #print ("initialization: ", is_sorted(l[0:0]))
    for i in xrange(1, len(l)):
        j = i - 1
        key = l[i]
        #solution is (j >= 0)
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
        #print ("maintenance: ", is_sorted(l[0:i]))
    #print ("termination: " , is_sorted(l[i:len(l)-1]))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print " ".join(map(str,ar))
