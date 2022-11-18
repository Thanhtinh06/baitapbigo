def getHightBook(lstTime,nBook,timeFree):
    maxBook = 0
    countBook = 0
    j = 0
    for i in range(nBook):
      while timeFree < lstTime[i]:
        timeFree += lstTime[j]
        j += 1
        countBook -= 1
        
      timeFree -= lstTime[i]
      countBook += 1
      maxBook = max(countBook,maxBook)
    return maxBook

  
nBook, timeFree = map(int,input().split())
lstTime = list(map(int,input().split()))
print(getHightBook(lstTime,nBook,timeFree))