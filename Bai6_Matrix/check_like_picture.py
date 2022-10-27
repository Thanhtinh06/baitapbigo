def check_like_picture(a, nrows, ncols):
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            if a[i][j] > 100:
                count += 1
    return count


a = []
nrows, ncols = map(int, input().split())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    a.append(value_row)

print(check_like_picture(a, nrows, ncols))
