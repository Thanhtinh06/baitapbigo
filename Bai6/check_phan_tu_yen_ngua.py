def check_yen_ngua(a, nrows, ncols):
    count = 0
    for i in range(nrows):
        max_row = max(a[i])
        for j in range(ncols):
            if a[i][j] == max_row:
                cols = []
                for m in range(nrows):
                    cols.append(a[m][j])
                min_col = min(cols)
                if max_row == min_col:
                    count += 1
    return count


a = []
nrows, ncols = map(int, input().split())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    a.append(value_row)

print(check_yen_ngua(a, nrows, ncols))
