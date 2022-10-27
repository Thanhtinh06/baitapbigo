
n = int(input())
flag = "YES"

for i in range(0, n):
    x = int(input())
    if x % 2 == 0:
        continue
    else:
        flag = "NO"

print(flag)
