class Solution:
    def mySqrt(self, x: int) -> int:
          n = x // 2
          i = 1
          if x == 0:
               i = 1
          elif x < 4:
               i = 2
          elif x == 5:
               i = 3
          else:
                    
               try:
                    if (n*n) >= x:
                         while x//(i*i) > 0:
                              i += 1
               except:
                    i = i = 1
          return i-1

x = 1341078699
sol = Solution()
print(sol.mySqrt(x))