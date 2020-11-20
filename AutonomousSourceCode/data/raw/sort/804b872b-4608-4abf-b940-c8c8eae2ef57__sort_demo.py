
# A sort function should return a negative value if a should be 'before'
# b in the sort order, zero if they are equal, or a positive value if a 
# should be 'after' b in the sort order


def mySortFunction(a,b):
    return a[1]-b[1]


myListofLists=[[8,9,3],[1,1,5],[4,5,0],[3,4,9],[6,3,1]]


print sorted(myListofLists)

print sorted(myListofLists,cmp=mySortFunction)