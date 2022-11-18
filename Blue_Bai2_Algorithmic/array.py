def getArray(lst,n,k):
    i = 0 
    l = r = -1
    unique = 0
    lstCountDigit = [0] * (10 ** 5 + 5)
    j = 0
    while i < n:
      if lstCountDigit[lst[i]] == 0:
        unique += 1
      lstCountDigit[lst[i]] += 1
      i += 1
      while unique == k:
          lstCountDigit[lst[j]] -= 1
          if lstCountDigit[lst[j]] == 0:
              l = j + 1
              r = i 
              return l,r  
          j += 1
    return l,r
  
n, k = map(int,input().split())
lst = list(map(int,input().split()))
l,r = getArray(lst,n,k)
print(l,r)