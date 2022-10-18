# import sys
# sys.setrecursionlimit(10003)
# De qui


def find_num_max(n, max):
    digit = n % 10
    if n == 0:
        return max
    if digit > max:
        max = digit
    return find_num_max(n//10, max)


n = int(input())
print(find_num_max(n, 0))


# Khong de qui
# def find_num_max(n):
#     digit_max = 0
#     while n > 0:
#         digit = n % 10
#         if digit >= digit_max:
#             digit_max = digit
#         n //= 10
#     return digit_max
