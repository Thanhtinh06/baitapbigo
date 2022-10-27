n = int(input())
a = list(map(int, input().split()))
result = True

for i in range(n):
    if a[i] == 0:
        result = False
        break

if result == True:
    print("YES")
else:
    print("NO")
