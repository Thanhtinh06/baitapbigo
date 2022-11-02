def findPositionX(lst,x,n):
  for i in  range(n):
    if lst[i] == x:
      return i
  return -1

n, x = map(int,input().split())
lst = list(map(int,input().split()))
print(findPositionX(lst,x,n))
