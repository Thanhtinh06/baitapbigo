def check_count_num(n):
    result = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0
    for char in n:
        if char in result:
            count += 1
    return count


n = input()
print(check_count_num(n))
