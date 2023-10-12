from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
          if arr[i] == 0:
            arr.insert(i+1,0)
            arr.pop()
            i += 1
          i += 1
 
nums = [1,0,2,3,0,4,5,0] 
Solution.duplicateZeros(Solution,nums)
print(nums)         