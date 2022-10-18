def check_nam_cham(a, n):
    flag = True
    var = a[0]
    count = 1
    for i in range(1, len(a)):
        if a[i] != var:
            var = a[i]
            count += 1
    return count


a = []
n = int(input())
for j in range(n):
    value_row = input()
    a.append(value_row)

print(check_nam_cham(a, n))
