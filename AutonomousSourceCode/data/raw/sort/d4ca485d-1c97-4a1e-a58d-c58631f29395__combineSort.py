'''
Created on 2013-6-8

@author: Brilliant
'''
def combine2SortedLists(List1, List2):
    if len(List1)> 0 and len(List2)> 0:
        if List1[ 0]>List2[ 0]:
            return [List2[ 0]]+combine2SortedLists(List1, List2[ 1:])
        elif List1[ 0]<List2[ 0]:
            return [List1[ 0]]+combine2SortedLists(List1[ 1:], List2)
        else:
            return [List1[ 0], List2[ 0]]+combine2SortedLists(List1[ 1:], List2[ 1:])
    elif len(List2)== 0:
        return List1
    elif len(List1)== 0:
        return List2
       
def combineSort(List1):
    NewList1=[]
    for value in List1:
        NewList1.append([value])
    return do_combineSort(NewList1)
       
def do_combineSort(ListsOfList=[]):
    if len(ListsOfList) == 1:
        return ListsOfList[ 0]

    i = 1
    Result = []   
    while i < len(ListsOfList):
        Result.append(combine2SortedLists(ListsOfList[i- 1], ListsOfList[i]))
        i+= 2
    if len(ListsOfList) % 2 == 1 :
        Result.append(ListsOfList[- 1])
    return do_combineSort(Result)

def merge2List(SortedList1 = [], SortedList2 = []):
    Result = []
    while True:
        if SortedList1 == []:
            return Result+SortedList2
        
        if SortedList2 == []:
            return Result+SortedList1
        
        v1 = SortedList1[0]
        v2 = SortedList2[0]
        if v1 > v2:
            Result.append(v2)
            SortedList2.pop(0)
        else:
            Result.append(v1)
            SortedList1.pop(0)

def mergeSort(unSortedList):
    if len(unSortedList) <= 1:
        return unSortedList
    
    Queue = []
    for v in unSortedList:
        Queue.append([v])
        
    while True:
        if len(Queue) == 1:
            return Queue[0]
        
        List1 = Queue.pop(0)
        List2 = Queue.pop(0)
        Queue.append(merge2List(List1, List2))
        
print( combine2SortedLists([1 ,2 ,3 ,4 ], [1 ,6 ,7 ,8 ]))
print( combineSort([6 ,5 ,4 ,3 ,2 ,1 ]))

print( merge2List([1 ,2 ,3 ,4 ], [1 ,6 ,7 ,8 ]))
print( mergeSort([6 ,5 ,4 ,3 ,2 ,1 ]))
Seq=range(1000,1,-2)+range(3000,4000)+range(2000,3000)
Seq.reverse()
print( mergeSort(Seq)) 
