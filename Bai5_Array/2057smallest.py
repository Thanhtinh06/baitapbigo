from typing import List
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
      for i in range(len(nums)):
        if i % 10 == nums[i]:
          return i
      return -1

nums = [1,2,3,4,5,6,7,8,9,0]
print(Solution.smallestEqual(Solution,nums))