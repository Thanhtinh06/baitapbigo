def calculate_factorial(n):
    if n <= 1:
        return 1
    ans = n * calculate_factorial(n-1)
    return ans


n = int(input())
print(calculate_factorial(n))
