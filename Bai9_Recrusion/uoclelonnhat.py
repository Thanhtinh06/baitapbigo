# ans = n % 2

# Cach khong de qui
# def greatest_common_divisor(n):
#     ans = 1
#     term = n
#     if term % 2 != 0:
#         ans = n
#     else:
#         while term > 0:
#             var = term // 2
#             if term % 2 == 0 and var % 2 != 0 and var > ans:
#                 ans = var
#             term //= 2
#     return int(ans)


# Cach de qui

def greatest_common_divisor(n):
    if n % 2 != 0:
        return n
    return int(greatest_common_divisor(n/2))


n = int(input())
print(greatest_common_divisor(n))
