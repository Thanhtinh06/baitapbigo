import sys
sys.setrecursionlimit(10**8)


class Solution:
    def tribonacci(self, n):
        if 0 < n < 3:
            return 1
        elif n == 0:
            return 0
        return self.tribonacci(self, n - 3) + self.tribonacci(self, n - 2) + self.tribonacci(self, n - 1)


n = int(input())
print(Solution.tribonacci(Solution, n))
