m, n = map(int, input().split())

if m % 2 == 0:
    count = n * (m//2)
else:
    count = n*(m//2) + n//2

print(int(count))
