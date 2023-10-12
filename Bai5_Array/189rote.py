from typing import List


class Solution:

    def reverse(self, nums, start, end):
      
        while start < end:
            term = nums[start]
            nums[end] = nums[start]
            nums[start] = term
            start += 1
            end += 1

    def rotate(self, nums: List[int], k: int) -> None:

        i = 0
        while i <= k:
          Solution.reverse(Solution,nums,i,k+1)
          i += 1
          k += 1

nums = [-1, -100, 3, 99]
k = 2
print(Solution.rotate(Solution, nums, k))
