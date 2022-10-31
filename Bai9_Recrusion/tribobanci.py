import sys
sys.setrecursionlimit(10**8)


# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter


class Solution:
    memory = {}

    def memoize_factorial(self, n):

        # This inner function has access to memory
        # and 'f'
        def inner(num):
            if num not in self.memory:
                self.memory[num] = n(num)
            return self.memory[num]
        return inner

    def tribonacci(self, n):
        self.memoize_factorial(self, n)
        if 0 < n < 3:
            return 1
        elif n == 0:
            return 0
        return self.tribonacci(self, n - 3) + self.tribonacci(self, n - 2) + self.tribonacci(self, n - 1)


n = int(input())
print(Solution.tribonacci(Solution, n))
