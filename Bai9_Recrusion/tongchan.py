# De qui


def sum_even_number(a, index):
    sum = 0
    if index == 0 and a[index] % 2 == 0:
        return a[index]
    elif index == 0 and a[index] % 2 != 0:
        return 0
    else:
        if a[index] % 2 == 0:
            sum += a[index]
    return sum + sum_even_number(a, index-1)


n = int(input())
a = list(map(int, input().split()))
index = n - 1
print(sum_even_number(a, index))


# Khong de qui
# def sum_even_number(a):
#     sum = 0
#     for item in a:
#       if item % 2 == 0:
#         sum += item
#     return sum
