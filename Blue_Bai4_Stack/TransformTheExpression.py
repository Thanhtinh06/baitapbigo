class Stack:
    def __init__(self):
        self.stack = []
        
    def pop(self):
      if len(self.stack) < 1:
        return None
      return self.stack.pop()
    
    def push(self,item):
      self.stack.append(item)
      
    def size(self):
      return len(self.stack)

arrStr = []
n = int(input())
for i in range(n):
    string = input()
    arrStr.append(string)
 
ansStr = []    
for string in arrStr:   
    stack = Stack()
    symbol = ord(')')
    ans = ''
    for j in range(len(string)):
      if ord(string[j]) > 96:
        ans += string[j]
      elif  42 <= ord(string[j]) <= 94:
        stack.push(string[j])
      elif ord(string[j]) == symbol and stack.size() > 0:
        ans += stack.pop()
    ansStr.append(ans)
      
for string in ansStr:
  print(string)