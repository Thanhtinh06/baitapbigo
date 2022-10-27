# Khong de quy

# def covert_hexadecimal_number(n):
#     result = []
#     while n != 0:
#         if 10 <= n % 16 <= 15:
#             result.insert(0, chr(55 + n % 16))
#         result.insert(0, str(n % 16))
#         n //= 16
#     return result


# de quy


def convert2Hex(n):
    if n < 10:
        return n
    return chr(ord('A') + n - 10)


def convert_hexadecimal_number(n, result=''):

    if n == 0:
        if len(result) == 0:
            return 0
        return result
    result += str(convert2Hex(n % 16))
    return convert_hexadecimal_number(n//16, result)


n = int(input())
result = convert_hexadecimal_number(n)
if result == 0:
    print(result)
else:
    for i in range(len(result)-1, -1, -1):
        print(result[i], end="")
