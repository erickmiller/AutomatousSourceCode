#!/usr/bin/python
import sys
import random

class InsertSort():
    N = []
        
    def __init__(self,arr):
        self.N = arr
        
    def exchange(self, x, y):
        tmp = self.N[x]
        self.N[x] = self.N[y]
        self.N[y] = tmp
        
    def isSorted(self):
        return self.checkSorted(0,len(self.N)-1)
    
    def lessThan(self, i, j):
        if self.N[i] < self.N[j]:
            return -1
        
        if self.N[i] > self.N[j]:
            return 1
            
        return 0
        
    def checkSorted(self,low,high):
        if low>= high:
            return True

        for k in range(low,high):
            if self.N[k] > self.N[k+1]:
                print "array not sorted!"
                for kk in range(low,high+1):
                    print self.N[kk]
                return False

        return True
        
    def Sort(self):
        num = len(self.N)
        
        for i in range(1,num):
            for j in range(i,0,-1):
                #print self.N
                if self.lessThan(j,j-1) < 0:
                    self.exchange(j,j-1)
                else:
                    break

    def printN(self):
        print self.N

class ShellSort(InsertSort):
    def __init__(self,arr):
        InsertSort.__init__(self,arr)
        self.hSort = []
        i = 1
        while i < len(self.N):
            self.hSort.append()
            i = 3 * i + 1
        self.hSort.reverse()
        print "distance serial:",self.distance
    
    def Sort(self):
        #generate the 
        
        num = len(self.N)
        
        for h in self.hSort:
            for i in range(1,num,h):
                for j in range(i,0,(-1) * h):
                    #print self.N
                    if self.lessThan(j, j-h) < 0:
                        self.exchange(j, j-h)
                    else:
                        break
        
def CallSortAlg(func,arg=None):
    import time
    t1 = time.time()
    func()
    t2 = time.time()
    print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)

def InsertSortUnitTest():
    arrayN = []
    random.seed(10000000)
    
    for i in range(0,4000):
        arrayN.append(random.randint(1, 100000))

    print arrayN
    m = InsertSort(arrayN)
    res = CallSortAlg(m.Sort)
    m.printN()
    assert(m.isSorted())

InsertSortUnitTest()
