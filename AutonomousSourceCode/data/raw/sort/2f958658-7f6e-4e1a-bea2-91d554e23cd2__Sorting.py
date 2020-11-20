from operator import itemgetter

__author__ = 'george'


l1=[9,10,0,-5,111,2,4,3,5,2,8]

print l1.sort()
print l1

l1=[9,10,0,-5,111,2,4,3,5,2,8]

print sorted(l1)
print l1
print sorted(l1,reverse=True)

tup= (1,5,32,6,0,-12)
print sorted(tup)

def keyfunc(A):
    return A[0]

A=[[1,2],[5,3],[0,1],[-10,3]]
A.sort(key=keyfunc)
print A
A.sort(key=keyfunc,reverse=True)
print A


#Lambda
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
sorted(student_tuples, key=itemgetter(1,2))