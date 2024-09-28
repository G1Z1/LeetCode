from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

     for i in range(0,len(nums)):
          for j in range(0,len(nums)):
               if i == j:
                    continue
               if  nums[i]+nums[j]==target:
                    sList = [j,i]
     return sList
     
nums = [2,7,11,15]
target = 9
s = Solution()
s = s.twoSum(nums,target)

print(s)