
n = int(input())
space = n - 2
str_space = space * ' '
i = 1
while i <= n:
    if i == 1 or i == n:
        print('*' * n)
    else:
        canh_trong = '*' + str_space + '*'
        print(canh_trong)
    i += 1
