def check_study_hour(n, a):
    count = 0
    for i in range(n):
        if a[i] == 0:
            count += 1
        else:
            count = 0
        if count > 3:
            return False
    return count == 0


n = int(input())
a = list(map(int, input().split()))

if check_study_hour(n, a) == True:
    print("YES")
else:
    print("NO")
