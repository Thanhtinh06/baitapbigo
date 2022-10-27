# Khong de quy
# def convert_binary(n):
#     result = 0
#     i = 1
#     while n != 0:
#         result += (n % 2) * i
#         n //= 2
#         i *= 10
#     return result
# n = int(input())
# print(convert_binary(n))


def convert_binary_number(n, i=1):
    if n == 0:
        return n % 2
    return convert_binary_number(n//2, i*10) + n % 2 * i


n = int(input())
print(convert_binary_number(n))
