import sys
sys.setrecursionlimit(10**8)


class Solution:
    def tribonacci(self, n):
        if 0 < n < 3:
            return 1
        elif n == 0:
            return 0
        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)


n = int(input())
print(Solution.tribonacci(n))
