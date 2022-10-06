def print_tong_rows(a, nrows, ncols):

    for i in range(nrows):
        sum = 0
        for j in range(ncols):
            sum += a[i][j]
        print(f"{i}: {sum}")


a = []
nrows, ncols = map(int, input().split())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    a.append(value_row)

print_tong_rows(a, nrows, ncols)
