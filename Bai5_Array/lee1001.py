from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
      i = j = 0
      for i in range(len(nums)):
        if nums[i] == 0:
          k -= 1
          
        if k < 0:
          if nums[j] == 0:
            k += 1
          j += 1
      return i - j + 1

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(Solution.longestOnes(Solution,nums,k))
