def getHigght(num1,num2,num3):
  lst = []
  maxLst = 0
  lst.append(num1 + num2 + num3)
  lst.append(num1 * num2 + num3)
  lst.append(num1 + num2 * num3)
  lst.append((num1 + num2) * num3)
  lst.append(num1 * (num2 + num3))
  lst.append(num1 * num2 * num3)
  maxLst = max(lst)
  return maxLst

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(getHigght(num1,num2,num3))