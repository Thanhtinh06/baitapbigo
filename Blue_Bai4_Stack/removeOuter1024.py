# import queue
# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#       count = 0
#       strAns = ''
#       q = queue.Queue()
#       for i in range(len(s)):
#         if s[i] == '(':
#           count += 1
#           q.put(s[i]) if count != 1 else q
#         if s[i] == ')':
#           count -= 1
#           q.put(s[i]) if count != 0 else q
#         if count == 0 and q.qsize() > 0:
#           while q.qsize() > 0:
#             strAns += q.get()
#       return strAns
    
#Cach2: 
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
      count = 0
      strAns = ''
      for i in range(len(s)):
        if s[i] == '(':
          count += 1
          if count > 1:
            strAns += s[i] 
        if s[i] == ')':
          count -= 1
          if count != 0:
            strAns += s[i]
      return strAns

s = '(()())(())'
print(Solution.removeOuterParentheses(Solution,s))

#Cach 3:
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = []
        stack = []
        
        for x in s:
            if x == "(":
                if stack:
                    answer.append("(")
                stack.append("(")
            elif x == ")":
                stack.pop()
                if stack:
                    answer.append(")")
        
        return "".join(answer)
      