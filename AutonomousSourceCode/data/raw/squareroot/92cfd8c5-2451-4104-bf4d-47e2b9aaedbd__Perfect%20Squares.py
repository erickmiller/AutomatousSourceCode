import math
class Solution(object):
    def f(self, dict, n):                   #Solve the problem recursively.
        if n == 0:                          #If n is 0, return 0.
            return 0
        if n in dict:                       #If the result of n is already in the dict, return dict[n].
            return dict[n]
        m = 0x7fffffff                      #Use m to store the least number of perfect square numbers。
        t = int(math.sqrt(n))               #The upper bound of squre root to traverse sqrt(n).
        k = max(int(math.sqrt(n / 3)), 1)   #The lower bound of squre root to traverse max(sqrt(n/3), 1).
        while t >= k:
            a = self.f(dict, n - t * t)     #Get the result of n - t^2.
            if a == 0:                      #If n - t^2 is a square number, return 1.
                return 1
            if a < m:
                m = a
            t -= 1
        dict[n] = m + 1                     #Store intermedia results in dict.
        return m + 1
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict = {}                           #Use dict to store intermedia results.
        return self.f(dict, n)
