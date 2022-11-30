def getHightAndCountTowers(arr,n):
    arr.sort()
    fre = [0] * 1005
    count = 0
    hight = 0
    for i in range(n):
      if arr[i] != arr[i-1]:
        count += 1
      fre[arr[i]] += 1
      hight = max(hight,fre[arr[i]])
    if count == 0:
      count = 1
    return hight,count

n = int(input())
arr = list(map(int,input().split()))
hight,count = getHightAndCountTowers(arr,n)
print(hight,count)