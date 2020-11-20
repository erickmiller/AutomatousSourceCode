import random

def CreateRandomList(size):
    lst = []
    for i in range(size):
        rNum = random.randrange(size)
        lst.append(rNum)
    return lst

def BubbleSort(rList):
    flag = True 
    while flag:
        flag = False
        for i in range(len(rList) - 1):
            if rList[i] < rList[i+1]:
                num1 = rList[i]
                num2 = rList[i+1]
                rList[i] = num2
                rList[i+1] = num1
                flag = True
    return rList
                
def CompareSortedLists(rListCopySorted, bubbleSortedList):
    if rListCopySorted == bubbleSortedList:
        print 'Sorted rListCopy is equal to bubbleSortedList'
    else:
        print 'rList and rListCopy not equal...'



def main():
    size = 100
    bubbleSortList = []
    rList = CreateRandomList(size)
    rListCopy = rList[:]
    rListCopy.sort(reverse = True)
    print rListCopy
    bubbleSortList = BubbleSort(rList)
    print bubbleSortList
    CompareSortedLists(rListCopy, bubbleSortList)
    
    
main()

