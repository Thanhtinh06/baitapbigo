def check_so_hoang_hau(a, nrows):
    count = 0
    lst_cheo_chinh = []
    lst_cheo_phu = []
    for i in range(nrows):
        lst_cheo_chinh.append(a[i][i])
        lst_cheo_phu.append(a[i][nrows-i-1])
    max_cheo_chinh = max(lst_cheo_chinh)
    max_cheo_phu = max(lst_cheo_phu)

    for i in range(nrows):
        max_row = max(a[i])
        for j in range(nrows):
            if a[i][j] == max_row:
                cols = []
                for m in range(nrows):
                    cols.append(a[m][j])
                max_col = max(cols)
                if i == j or j == nrows - i - 1:
                    if (max_col == max_cheo_chinh == max_row) or (max_col == max_cheo_phu == max_row):
                        count += 1
                        print(a[i][j])
                else:
                    if max_row == max_col:
                        count += 1
                        print(a[i][j])

    return count


a = []
nrows = int(input())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    a.append(value_row)

print(check_so_hoang_hau(a, nrows))
