def findX(arr,a,b,n):
    #bubble Short
    for i in range(n):
      for j in range(n-1):
        if arr[j] > arr[j+1]:
          arr[j],arr[j+1] = arr[j+1],arr[j]
    count = abs(arr[-a] - arr[b-1])
    return count

n,a,b = map(int,input().split())
arr = list(map(int,input().split()))
print(findX(arr,a,b,n))