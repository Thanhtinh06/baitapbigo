class Solution: 
  def solve(self,A, B):
    N = len(A[0])
    P = [[0] * (N+1) for i in range(N+1)]
    
    for i in range(1, N+1):
      for j in range(1, N+1):
        P[i][j] = A[i - 1][j - 1] + P[i - 1][j] + P[i][j-1] - P[i - 1][j-1]
    
    max_value = float('-inf')
    
    for i in range(B,N+1):
      for j in range(B,N+1):
        sumSubMatrix = P[i][j] - P[i][j-B] - P[i-B][j] + P[i-B][j-B]
        max_value = max(max_value,sumSubMatrix)
    return max_value

A = [[1, 1, 1, 1, 1],
     [2, 2, 2, 2, 2],
     [3, 8, 6, 7, 3],
     [4, 4, 4, 4, 4],
     [5, 5, 5, 5, 5]]

P = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     ]
print(Solution.solve(Solution, A, 3))