class Edge:
    def __init__(self,u,v):
        self.u = u
        self.v = v
      
    
lstEdge = []
adjMatrix = []
nrows = int(input())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    adjMatrix.append(value_row)

flag = True
for i in range(nrows):
  for j in range(nrows):
    if adjMatrix[i][j] != adjMatrix[j][i]:
      flag = False
      break

if flag:
  print('YES')
else:
  print('NO')

    


  