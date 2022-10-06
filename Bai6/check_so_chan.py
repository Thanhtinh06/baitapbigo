def check_so_chan(a, nrows, ncols):
    index = 0
    count_max = 0
    for i in range(0, nrows):
        count = 0
        for j in range(ncols):
            if a[i][j] % 2 == 0:
                count += 1
        if count != 0 and count > count_max:
            index = i
            count_max = count

    return index


a = []
nrows, ncols = map(int, input().split())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    a.append(value_row)

print(check_so_chan(a, nrows, ncols))
