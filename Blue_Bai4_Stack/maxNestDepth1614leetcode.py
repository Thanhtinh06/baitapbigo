class Solution:
    def maxDepth(self, s: str) -> int:
      countMax = 0
      count = 0
      stack = []
      for i in range(len(s)):
        if s[i] == '(':
          stack.append(s[i])
          count += 1
        elif s[i] == ')':
          count -= 1
          stack.pop()
        countMax = max(count,countMax)
      return countMax

s = "(1+(2*3)+((8)/4))+1"
print(Solution.maxDepth(Solution,s))