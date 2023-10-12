from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
      codition = ["C","D","+"]
      result = []
      for ope in operations:
        if ope not in codition:
          result.append(int(ope))
        elif ope == "C" and len(result) > 0:
          result.pop()
        elif ope == "D" and len(result) > 0:
          newValue = (int(result[-1]) * 2)
          result.append(newValue)
        elif ope == "+" and len(result) > 1:
          newValue = (int(result[-1]) + int(result[-2]))
          result.append(newValue)
        
      return sum(result)
    

ops = ["5","+"]
print(Solution.calPoints(Solution,ops))