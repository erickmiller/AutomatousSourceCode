def turboSort():
    inputValue = int(raw_input())
    sortedList = []
    for each in range(inputValue):
        number =  int(raw_input())
        lastIndex = len(sortedList) - 1
        if(lastIndex == -1 or (sortedList[lastIndex] <= number)):
            sortedList.append(number)
        elif(sortedList[0]>=number) :
            sortedList.insert(0,number)
        else:
            addToList(number,sortedList)
        print sortedList
    for each in sortedList:
        print each
def addToList(number,sortedList):
    print "add to list start"
    lower = 0
    higher = len(sortedList) - 1
    while(lower!=higher):
        mid = 0
        if((lower + higher)% 2 == 0 ):
            mid = (lower + higher)/2
        else:
            mid = (lower + higher)/2 + 1
        print lower, higher, mid
        if(sortedList[mid] == number):
            sortedList.insert(mid,number)
            return
        elif(sortedList[mid] < number):
            lower = mid+1
        else:
            higher = mid - 1
    print "while ends"
    print lower, higher
    sortedList.insert(higher,number)
        
turboSort()

        
