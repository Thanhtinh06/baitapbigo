def check_row_col(list_a):
    result = [0 for i in range(0, 9)]
    for var in list_a:
        result[var-1] += 1

    for item in result:
        if item != 1:
            return False
    return True


def creat_list_item_tam(a):
    list_tam = [1, 4, 7]
    list_a = []
    for j in list_tam:
        for i in list_tam:
            start_row = i - 1
            end_row = i + 1
            start_col = j - 1
            end_col = j + 1
            item_tam = []
            for row in range(start_row, end_row + 1):
                for col in range(start_col, end_col+1):
                    item_tam.append(a[row][col])
            list_a.append(item_tam)
    return list_a


def creat_list_col(a):
    list_col = []
    for j in range(9):
        col = []
        for i in range(9):
            col.append(a[i][j])
        list_col.append(col)
    return list_col


def check_sudoku(a):
    list_col = creat_list_col(a)
    list_item_tam = creat_list_item_tam(a)
    for item in a:
        if check_row_col(item) == False:
            return False

    for item in list_col:
        if check_row_col(item) == False:
            return False

    for item in list_item_tam:
        if check_row_col(item) == False:
            return False
    return True


a = []
for j in range(9):
    value_row = list(map(int, input().split()))
    a.append(value_row)

if check_sudoku(a):
    print('YES')
else:
    print('NO')
