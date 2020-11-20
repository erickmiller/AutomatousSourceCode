import numpy as np
import random
R = random.sample(range(0,100000), 100000)
random.R = random.choice(R)

#original sort function
def sortwithloops():
    sortedInput = list(R)
    swap = True
    while(swap == True):
        swap = False 
        for i in range(len(sortedInput)-1):
            if sortedInput[i] > sortedInput[i+1]:
                swap = True
                temp = sortedInput[i]
                sortedInput[i] = sortedInput[i+1]
                sortedInput[i+1] = temp
    return sortedInput

# numpy sort
def numpySort():
    newR = list(R)
    return np.sort(newR)

#sorted with pythons built in function (question 2 from HW 1)
def sortwithoutloops():
    newR2 = list(R)
    newR2.sort()
    return newR2

#search with loop (question 3 from hw 1)
def searchwithloops():
    for i in range(len(R)):
        if random.R == R[i]:
            return True
    return False

#search without a loop (question 4 from hw 1)
def searchwithoutloops():
    return random.R in R

    
#numpy search
def numpySearch():
    return random.R in np.array(R)
    
'''
if you look at my results you see my numpy search is pretty significantly slower than my search without loops.
what would cause that?
'''



if __name__ == "__main__":
    import timeit as ti
    print "Using 100 iterations for each\n\n"
    #print "Sort with loops: " + str(ti.timeit("sortwithloops()", setup="from __main__ import sortwithloops", number=100))
    print "Sort without loops: " + str(ti.timeit("sortwithoutloops()", setup="from __main__ import sortwithoutloops", number=100))
    print "Sort with numpy: " + str(ti.timeit("numpySort()", "from __main__ import numpySort", number=100))
    print "Search with loops: " + str(ti.timeit("searchwithloops()", setup="from __main__ import searchwithloops", number=100))
    print "Search without loops: " + str(ti.timeit("searchwithoutloops()", setup="from __main__ import searchwithoutloops", number=100))
    print "Search with numpy: " + str(ti.timeit("numpySearch()", setup="from __main__ import numpySearch", number=100))
