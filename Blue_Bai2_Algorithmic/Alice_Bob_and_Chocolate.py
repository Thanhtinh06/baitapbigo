def getCountAliceBobChoco(lstChoco,n):
    
    timeA = 0
    timeB = 0
    i = 1
    j = n - 2
    while i <= j:
      
      if timeA + lstChoco[i] <= timeB + lstChoco[j]:
        timeA += lstChoco[i]
        i += 1
      else:
        timeB += lstChoco[j]
        j -= 1 
    return i, j


n = int(input())
lstChoco = list(map(int,input().split()))
chocoOfAlice,chocoOfBob = getCountAliceBobChoco(lstChoco,n)
print(chocoOfAlice,chocoOfBob)