def getPositionBigSegment(lstLi,lstRi):
    minSegment = min(lstLi)
    maxSegment = max(lstRi)
    count = 1
    for i in range(len(lstLi)):
      if lstLi[i] == minSegment and lstRi[i] == maxSegment:
        return count
      count += 1
    return -1

amountSegment = int(input())
lstLi = []
lstRi = []
for i in range(amountSegment):
  l,r = map(int,input().split())
  lstLi.append(l)
  lstRi.append(r)
  
  
print(getPositionBigSegment(lstLi,lstRi))