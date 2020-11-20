class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        length = len(A)
        A[0:length] = sorted(A[0:length])

###########################################################################
#                              Testing Cases                              #
###########################################################################
if __name__ == "__main__":
    s = Solution()
    arr = [0, 1, 2, 0, 1, 1, 0, 1, 2, 0, 1]
    s.sortColors(arr)
    print arr
