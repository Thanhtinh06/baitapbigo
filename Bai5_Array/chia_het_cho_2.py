n = int(input())
a = list(map(int, input().split()))
result = []

for i in range(n):
    if a[i] % 2 == 0:
        result.append(a[i])

print(result)
