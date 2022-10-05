x = int(input())

divisorCount = 0
for i in range(1, ((x + 1) // 2)+1):
    if x % i == 0:
        divisorCount += 1
if divisorCount != 1 or x == 1:
    print('NO')
else:
    print('YES')
