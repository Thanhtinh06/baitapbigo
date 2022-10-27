
# x = int(input())

# remainder = x % 5

# if x <= 5:
#     step = 1
# else:
#     step = x // 5 + remainder // 4 + \
#         (remainder % 4) // 3 + (remainder % 4 %
#                                 3) // 2 + (remainder % 4 % 3 % 2) // 1

# print(step)

# cach 2

x = int(input())

if x % 5 == 0:
    step = x / 5
else:
    step = x // 5 + 1

print(int(step))
