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
    
    def valueLastStack(self):
      return self.stack[-1]

while True:
    n = int(input())
    if n == 0:
        break
    trucks = list(map(int, input().split()))
    stack = Stack()
    ordering = 1
    i = 0

    while i < n:
        if trucks[i] == ordering:
            ordering += 1
            i += 1
        elif stack.size() > 0 and stack.valueLastStack() == ordering:
            ordering += 1
            stack.pop()
        else:
            stack.push(trucks[i])
            i += 1
    
    while stack.size() > 0 and stack.valueLastStack() == ordering:
        ordering += 1
        stack.pop()
    
    print('yes' if ordering == n + 1 else 'no')