def check_so_hoang_hau(a, nrows):
    # Check element max in row
    element_max_row = []
    for i in range(nrows):
        max_row = max(a[i])
        for j in range(nrows):
            if a[i][j] == max_row:
                element_max_row.append((a[i][j], i, j))

    # Check element max in row and col:
    element_max_in_row_col = []
    for element in element_max_row:
        max_element = element[0]
        index_col = element[2]
        result = True
        for i in range(0, nrows):
            if a[i][index_col] > max_element:
                result = False

        if result == True:
            element_max_in_row_col.append(element)

    # check element max in cross
    max_index = nrows - 1
    count = 0

    for element in element_max_in_row_col:
        index_col = element[2]
        index_row = element[1]
        element_value = element[0]
        row_start_cross_left = max(index_row - index_col, 0)
        col_start_cross_left = max(0, index_col - index_row)

        row_start_cross_right = max(index_col - (max_index - index_row), 0)
        col_start_cross_right = min(max_index, index_row + index_col)

        is_max_cross = True

        # Cross left
        while row_start_cross_left <= max_index and col_start_cross_left <= max_index:
            if element_value < a[row_start_cross_left][col_start_cross_left]:
                is_max_cross = False
                break
            row_start_cross_left += 1
            col_start_cross_left += 1

        # Cross right
        while row_start_cross_right <= max_index and col_start_cross_right >= 0:
            if element_value < a[row_start_cross_right][col_start_cross_right]:
                is_max_cross = False
                break
            row_start_cross_right += 1
            col_start_cross_right -= 1

        if is_max_cross == True:
            count += 1

    return count


a = []
nrows = int(input())

for i in range(nrows):
    value_row = list(map(int, input().split()))
    a.append(value_row)

print(check_so_hoang_hau(a, nrows))
