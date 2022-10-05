def check_student(n, a):

    count_female = 0
    count_male = 0
    if len(a) % 2 != 0:
        return False
    else:
        for i in range(n):
            if a[i] == 0:
                count_male += 1
            else:
                count_female += 1
        else:
            if count_female == count_male:
                return True
            else:
                return False


n = int(input())
a = list(map(int, input().split()))

if check_student(n, a) == True:
    print("YES")
else:
    print("NO")
