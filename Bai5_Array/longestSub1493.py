from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
      k = 1
      i = j = 0
      for i in range(len(nums)):
        if nums[i] == 0:
          k -= 1
          
        if k < 0:
          if nums[j] == 0:
            k += 1
          j += 1
      return i - j
    
print(Solution.longestSubarray(Solution,[0,1,1,1,0,1,1,0,1]))