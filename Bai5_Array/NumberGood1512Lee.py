from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
      count = 0
      for i in range(len(nums)):
        for j in range(i,len(nums)):
          if nums[i] == nums[j] and i < j:
            count += 1
      return count
    
nums = [1,2,3,1,1,3]
print(Solution.numIdenticalPairs(Solution,nums))