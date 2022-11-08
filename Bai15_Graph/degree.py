adjMatrix = []
nrows,x = map(int,input().split())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    adjMatrix.append(value_row)

count = 0
for i in range(x,x+1):
  for j in range(nrows):
    if adjMatrix[i][j] != 0:
      count += 1
print(count)