import queue

n, b = map(int,input().split())
queries = queue.Queue()
processing = 0
ans = []
 
for i in range(n):
    t,d = map(int,input().split())
    
    while queries.qsize() != 0 and t >= queries.queue[0]:
        queries.get()
 
    if queries.qsize() <= b: 
      processing = max(t,processing) + d
      queries.put(processing)
      ans.append(processing)
    else:
      ans.append(-1)
   
for time in ans:
  print(time,end=" ")
  
# n, b = map(int, input().split())
# q = queue.Queue()
# processing = 0

# for i in range(n):
#     t, d = map(int, input().split())

#     while q.qsize() != 0 and t >= q.queue[0]:
#         q.get()

#     if q.qsize() <= b:
#         processing = max(t, processing) + d
#         q.put(processing)
#         print(processing, end=' ')
#     else:
#         print(-1, end=' ')