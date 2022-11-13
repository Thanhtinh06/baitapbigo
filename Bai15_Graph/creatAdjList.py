class Edge:
    def __init__(self,u,v):
        self.u = u
        self.v = v
    
    def __str__(self) -> str:
        return '{0} {1}'.format(self.u,self.v)
  
    
lstEdge = []
adjMatrix = []
adjList = []
nrows = int(input())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    adjMatrix.append(value_row)

for i in range(nrows):
  for j in range(nrows):
    if adjMatrix[i][j] == 1:
      lstEdge.append(Edge(i,j))

print(len(lstEdge))
for edge in lstEdge:
  print(edge)