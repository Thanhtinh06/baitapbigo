def checkSymmetryString(lst, n, indexFirst, indexLast, flag):
    if indexFirst == n // 2:
        return flag
    if lst[indexFirst] != lst[indexLast]:
        flag = False
            
    return checkSymmetryString(a, n, indexFirst + 1, indexLast - 1, flag)


n = int(input())
lst = input()
indexFirst = 0
indexLast = n - 1
if checkSymmetryString(a, n, indexFirst, indexLast, True):
    print('YES')
else:
    print('NO')