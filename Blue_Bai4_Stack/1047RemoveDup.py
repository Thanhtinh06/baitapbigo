
class Solution:
    def removeDuplicates(self, s):
      stack = []
      result = ""
      for char in s:
        if len(stack) == 0 or char != stack[-1]:
          stack.append(char)
        elif char == stack[-1]:
          stack.pop()
            
      return result.join(stack)
        
        
s = "abbaca"
result = Solution()
print(result.removeDuplicates(s))        
        
        
        
