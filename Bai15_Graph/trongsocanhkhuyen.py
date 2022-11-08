class Edge:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w
  
    
lstEdge = []
n = int(input())
count = 0
result = 1

for i in range(n):
    u,v,w = list(map(int, input().split()))
    lstEdge.append(Edge(u,v,w))

for edge in lstEdge:
  if edge.u == edge.v:
    count += 1
    result *= edge.w
    
if count == 0:
  print(-1)
else:
  print(count, result % (10 ** 6 + 7), end=" ")