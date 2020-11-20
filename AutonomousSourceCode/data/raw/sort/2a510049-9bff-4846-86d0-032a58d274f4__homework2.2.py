# Homework 2.2 - Tutorial 2 - Week 1
import operator


def sortFirst(L):
    return sorted(L,key=operator.itemgetter(0))

def sortThird(L):
    return sorted(L,key=operator.itemgetter(2))

def sortSecondDescend(L):
    return sorted(L,key=operator.itemgetter(1),reverse=True)

if __name__ == '__main__':
    L = [(1,2,3),(4,1,5),(0,0,6)]
    print(sortFirst(L))
    print(sortThird(L))
    print(sortSecondDescend(L))
