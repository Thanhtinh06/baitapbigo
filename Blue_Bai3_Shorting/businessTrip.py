k = int(input())
arr = list(map(int,input().split()))
countMonth = 0
arr.sort(reverse=True)
sumMonth = 0

for month in arr:
  if sumMonth >= k:
    break
  countMonth += 1
  sumMonth += month
if countMonth == len(arr) and sumMonth < k:
  print(-1)
else:
  print(countMonth)
    