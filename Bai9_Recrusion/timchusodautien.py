
# Khong dung de quy
# def find_first_char(n):
#     term = n
#     char = 0
#     while term > 10:
#         term //= 10
#         char = term
#     return char


# Dung de quy
def find_first_char(n):

    if n < 10:
        return n
    return find_first_char(n//10)


n = int(input())
print(find_first_char(abs(n)))
