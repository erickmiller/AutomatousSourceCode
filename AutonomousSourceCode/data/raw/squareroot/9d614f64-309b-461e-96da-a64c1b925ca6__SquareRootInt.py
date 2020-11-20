class Solution:
   # Time: O(logn)
   # Space: O(1)
   def squareRootInt(self, x):
      if x <= 1: return x
      l, r = 0, x
      while l + 1 < r:
         mid = l + ((r - l) >> 1)
         if mid * mid == x: return mid
         elif mid * mid < x: l = mid
         else: r = mid - 1
      return r if r * r <= x else l

if __name__ == "__main__":
   t = Solution()
   for i in range(10):
      print t.squareRootInt(i),
