def getAmoutVest(lstExcept,lstValid,n,m,x,y):
    ans = []
    i = j = 0
    while i < m:
      if j >= n:
          break
      if (lstExcept[j] - x) <= lstValid[i] <= (lstExcept[j] + y):
        ans.append([j+1,i+1])
        j += 1
        i += 1
      elif lstValid[i] > lstExcept[j] + y:
        j += 1
      elif lstValid[i] < lstExcept[j] - x:
        i += 1

    return ans


n,m,x,y = map(int,input().split())
lstExcept = list(map(int,input().split()))
lstValid = list(map(int,input().split()))
ans = getAmoutVest(lstExcept,lstValid,n,m,x,y)
print(len(ans))
for item in ans:
  print(item[0],item[1])
