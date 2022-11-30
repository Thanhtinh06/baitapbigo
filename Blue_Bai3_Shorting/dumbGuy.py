def getMinTime(arr,n,x):
    arr.sort()
    minTime = 0
    for i in range(n):
      minTime += arr[i] * x
      if x > 1:
        x -= 1
    return minTime

n, x = map(int,input().split())
arr = list(map(int,input().split()))
print(getMinTime(arr,n,x))