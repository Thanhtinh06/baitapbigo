class Edge:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w
 
def merge(left, n1, right, n2, lstEdge, n):
    i = j = k = 0
    while i < n1 and j < n2:
        if left[i].w > right[j].w:
            lstEdge[k] = left[i]
            i += 1
        else:
            lstEdge[k] = right[j]
            j += 1
        k += 1
    while i < n1:
        lstEdge[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        lstEdge[k] = right[j]
        j += 1
        k += 1


def mergeShort(lstEdge, n):
    if n > 1:
        n1 = n // 2
        n2 = n - n1
        left = lstEdge[:n1]
        right = lstEdge[n1:]
        mergeShort(left, n1)
        mergeShort(right, n2)
        merge(left, n1,right, n2, lstEdge, n)
    return lstEdge
 
lstEdge = []
n, x = map(int,input().split())
count = 0

for i in range(n):
    u,v,w = list(map(int, input().split()))
    lstEdge.append(Edge(u,v,w))
    
ans = mergeShort(lstEdge,len(lstEdge))

for j in range(-x,0):
  print(ans[j].u, ans[j].v)