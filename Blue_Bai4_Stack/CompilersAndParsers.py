n = int(input())

for i in range(n):
  char = input()
  
  lenght = 0
  stack = []
  close = []
 
  for i in range(len(char)):
    if char[i] == '<':
      stack.append(char[i])
    elif len(stack) == 0:
      break
    else:
      stack.pop()
      if len(stack) == 0:
        lenght = i + 1
  print(lenght)