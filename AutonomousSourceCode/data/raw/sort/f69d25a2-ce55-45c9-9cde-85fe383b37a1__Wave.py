__author__ = 'cenk'

# def maximumGap(num):
#     if len(num) == 0:
#         return -1
#     if len(num) == 1:
#         return 0
#     toSort = []
#     for i in range(len(num)):
#         toSort.append((num[i],i))
#
#     B = sorted(toSort,key=lambda tup: tup[0])
#
#     length = len(toSort)
#     maxIndex = B[length - 1][1];
#
#     ans = 0;
#     for i in range(length -1)[::-1]:
#         ans = max(ans,maxIndex - B[i][1])
#         maxIndex = max(maxIndex,B[i][1])
#
#     return ans;
#
#
# print maximumGap([2,3,5,1,6])

#
# def maximumGap(A):
#     if len(A) == 1:
#         return 0
#     max = 0
#     length = len(A)
#     for i in range(length):
#         for j in range(i + 1,length)[::-1]:
#             if A[j] > A[i] and j -i > max:
#                 max = j - i
#             if length - i < max:
#                 return max
#
#     return max
#
# print maximumGap([2,3,5,1,6])

def maximumGap(A):
    if len(A) == 1:
        return 0
    B = []
    for index,i in enumerate(A):
        B.append((i,index))

    B = sorted(B,key=lambda tup: tup[0])

    indexes = [i[1] for i in B]

    ans = 0
    maxIndex =  indexes[len(indexes) -1]

    for i in range(0,len(indexes))[::-1]:

        ans = max(ans,maxIndex - indexes[i])
        maxIndex = max(maxIndex, indexes[i])

    return ans

print maximumGap([ 2,3,5,1,6 ])

#
# def wave(A):
#     sortedA = sorted(A)
#     for i in range(0,len(A) - 1,2):
#         tmp = sortedA[i]
#         sortedA[i] = sortedA[i+1]
#         sortedA[i+1] = tmp
#     return sortedA
#
# print wave([1,2,3,4,5])