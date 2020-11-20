'''
ref: https://github.com/SebasSujeen/Merge_sort/blob/master/merge_sort/merge_sort.py
'''

from prepare.base_class import *

def merge_tbuns(left,right):
    sorted=[] #array to store the sorted list
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i].oid < right[j].oid:
            sorted.append(left[i])
            i+=1
        elif left[i].oid == right[j].oid:
            if left[i].timestamp > right[j].timestamp:
                sorted.append(left[i])
            else:
                sorted.append(right[j])
            i+=1
            j+=1
        else:
            sorted.append(right[j])
            j+=1
    sorted+=left[i:]
    sorted+=right[j:]
    return sorted

def merge_update(li):
    if len(li)==1:
        return li
    middle=len(li)/2
    left_li=merge_update(li[:middle])
    right_li=merge_update(li[middle:])
    return merge_tbuns(left_li,right_li)



if __name__=="__main__":

    tbunList=\
        [TBUN(1,10,0),
         TBUN(1,5,0),
         TBUN(1,2,0),
         TBUN(1,3,0),
         TBUN(1,7,0),
         TBUN(1,4,0),
         TBUN(1,8,0),
         TBUN(1,9,0),
         TBUN(2,5,-1),
         TBUN(2,3,-1),
         TBUN(2,8,-1)
         ]

    sortedTBunList=merge_update(tbunList)

    for tbun in sortedTBunList:
        print str(tbun)+'\n'

