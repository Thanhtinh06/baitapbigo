def find_max_apple(n, a):
    list_apple = []
    list_orange = []
    for i in range(n):
        list_apple.append(a[i][0])
    max_apple = max(list_apple)
    count = 0
    index = list_apple.index(max_apple)
    for i in range(n):
        if max_apple == a[i][0]:
            count += 1
            list_orange.append(a[i][1])
        else:
            list_orange.append(0)
    else:
        if count == 1:
            return index + 1
        else:
            max_orange = max(list_orange)
            return list_orange.index(max_orange) + 1


n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

print(find_max_apple(n, a))
