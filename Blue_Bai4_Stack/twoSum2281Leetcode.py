from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
      totalStrength = 0
      j = len(strength)
      for i in range(len(strength)):
        totalStrength += strength[i] * strength[i]
        while j > i+1:
          totalStrength += min(strength[i:j]) * sum(strength[i:j])
          j -= 1
        j = len(strength)
      return totalStrength % (10**9 + 7)

strength = [13,13,12,12,13,12]
print(Solution.totalStrength(Solution,strength))