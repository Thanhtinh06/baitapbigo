# cach khong dung de quy

# def count_number(n):
#     count = 0
#     term = n
#     while term > 0:
#         count += 1
#         term //= 10
#     return count


def count_number(n):

    if n < 10:
        return 1
    return 1 + count_number(n//10)


n = int(input())
print(count_number(abs(n)))
