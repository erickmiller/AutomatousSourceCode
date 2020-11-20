class Solution:
   # Time: O(logx/esp)
   # Space: O(1)
   def squareRoot(self, x, esp):
      if self.compare(x, 1.0, esp) < 0:
         l, r = x, 1.0
      else:
         l, r = 1.0, x
      while self.compare(l, r, esp) == -1:
         mid = l + 0.5 * (r - l)
         if self.compare(mid * mid, x, esp) == 0:
            return mid
         elif self.compare(mid * mid, x, esp) == 1:
            r = mid
         else:
            l = mid
      return l

   def compare(self, a, b, esp):
      diff = (a - b) / b
      if diff < -esp: return -1
      return diff > esp

if __name__ == "__main__":
   t = Solution()
   for i in range(1, 10):
      print t.squareRoot(i * 1.0, 0.0001)
