def getCountPeopleLive(lstWrath,n):
  count = 0
  j = n - 1
  i = n - 1
  while i >= 0:
    j = min(j,i)
    lastKillPos = max(0,i - lstWrath[i])
    if j > lastKillPos:
      count += (j-lastKillPos)
      j = lastKillPos
    i -= 1
  return n - count

  
n = int(input())
lstWrath = list(map(int,input().split()))
print(getCountPeopleLive(lstWrath,n))