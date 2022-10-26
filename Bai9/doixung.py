# import sys
# sys.setrecursionlimit(100003)


def check_doi_xung(a, n, index_dau, index_cuoi, flag):
    if index_dau == n // 2:
        return flag
    else:
        if a[index_dau] == a[index_cuoi]:
            flag = True
        else:
            flag = False
    return check_doi_xung(a, n, index_dau + 1, index_cuoi - 1, flag)


n = int(input())
a = input()
index_dau = 0
index_cuoi = n - 1
if check_doi_xung(a, n, index_dau, index_cuoi, True):
    print('YES')
else:
    print('NO')
