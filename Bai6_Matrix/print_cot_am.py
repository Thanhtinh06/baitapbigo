def check_cols_am(a, nrows, ncols):
    for j in range(ncols):
        flags = True
        for i in range(nrows):
            if a[i][j] >= 0:
                flags = False
                break
        if flags == True:
            print(j, end=" ")


a = []
nrows, ncols = map(int, input().split())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    a.append(value_row)

check_cols_am(a, nrows, ncols)
