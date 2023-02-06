from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      n = len(digits)
      total = 0
      arr = []
      j = 1
      for i in range(n-1,-1,-1):
        total += digits[i] * j
        j *= 10
      total += 1
      while total > 0:
        arr.append(total%10)
        total //= 10
      arr.reverse()
      return arr


digits = [1,2,3]
print(Solution.plusOne(Solution,digits))

