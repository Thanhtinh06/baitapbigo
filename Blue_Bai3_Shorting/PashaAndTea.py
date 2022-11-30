def getMaximumWater(arr,nPer,capacity):
    sorted_arr = sorted(arr,reverse=True)
    minBoy = sorted_arr[nPer-1]
    minGirl = sorted_arr[len(sorted_arr) - 1]
    maxWater = 0
    if minBoy / 2 > minGirl:
      maxWater += minGirl * nPer + minGirl*2 * nPer
    else:
      maxWater += minBoy * nPer + minBoy / 2 * nPer   
    if capacity - maxWater < 0:
      return capacity 
    return maxWater  
  
n,cap = map(int,input().split())
arr = list(map(int,input().split())) 
ans = (getMaximumWater(arr,n,cap))
if ans % 1 == 0:
  print(int(ans))
else:
  print(ans)
  
