#Bubble Sort built in Python

import random

def createList(length):
    l = []
    i = 0
    while length > i:
        l.append(random.randint(0,length))
        i +=1
    return l

#print createList(10)

def isSorted(l):
    i = 1
    while i < len(l):
        if l[i - 1] > l[i]:
            return False
        i += 1
    return True

a = [3,2,1]
b = [1,2,3]

#print "Should be false: " 
#print isSorted(a)
#print "Should be true: "
#print isSorted(b)

def bubble(l):
    check = len(l) - 1
    while (check > 0):
        i = 0
        while i < check:
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
            i += 1
        #print l
        check -= 1
    return l

pre = createList(10)
print pre
post = bubble(pre)
print post
print isSorted(post)
