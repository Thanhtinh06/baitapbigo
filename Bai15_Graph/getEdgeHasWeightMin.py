class Edge:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w
  
    
lstEdge = []
n = int(input())
minWeight = 10**8
count = 0

for i in range(n):
    u,v,w = list(map(int, input().split()))
    lstEdge.append(Edge(u,v,w))
    if w <= minWeight:
      minWeight = w

for edge in lstEdge:
  if edge.w == minWeight:
    count += 1

print(count)