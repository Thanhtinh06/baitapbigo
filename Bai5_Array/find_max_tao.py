def find_max_apple(n, a):
    max_index = 0
    max_tui = a[max_index]
    for i in range(1, n):
        tao = a[i][0]
        cam = a[i][1]
        if tao > max_tui[0] or tao == max_tui[0] and cam > max_tui[1]:
            max_tui = a[i]
            max_index = i
    return max_index + 1


n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

print(find_max_apple(n, a))
