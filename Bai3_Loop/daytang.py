
flag = "YES"

term = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n < term:
        flag = "NO"
    term = n

print(flag)
