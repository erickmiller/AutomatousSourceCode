__author__ = 'kyu'

def sort(A):
    m=len(A)
    if len(A)<=1: return A
    else:
        L=A[:m]
        R=A[m:]

#O(len(A)+len(B))
def merge(A,B):
    res=[]
    ia=0
    ib=0
    while ia<len(A) and ib <len(B):
        if A[ia] <= B[ib]:
            res.append(A[ia])
            ia+=1
        else:
            res.append(B[ib])
            ib+=1
    return res+A[ia:]+B[ib:]

#O(n) ※O(n/2)+O(n/2)=O(n)
def msort(A):
    if len(A) <= 1: return A
    else:
        m=len(A)/2
        return merge(msort(A[:m],msort(A[m:])))
    #L=A[:m]
    #R=A[m:]
    #sortedL=msort(L)
    #sortedR=msort(R)
    #return merge(sortedL,sortedR)

def msortBasic(A):
    if len(A) <= 1: return A
    else:
        m=len(A)/2  #O(c)
        L=A[:m] #O(n/2)
        R=A[m:] #O(n/2)
        sortedL=msort(L)
        sortedR=msort(R)
        return merge(sortedL,sortedR)




