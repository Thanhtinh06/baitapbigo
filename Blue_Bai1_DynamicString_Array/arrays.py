
nArr1, nArr2 = map(int,input().split())
k,m = map(int,input().split())
array1 = list(map(int,input().split()))
array2 = list(map(int,input().split()))

if array1[k-1] < array2[nArr2-m]:
  print('YES')
else:
  print('NO')