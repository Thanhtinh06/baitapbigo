# num = int(input())

# sum_num = 0
# n = 10000
# i = 10
# while n >= 1:
#     sum_num += num // n % i
#     n /= i
# point = int(sum_num % i)
# print(point)

# cach 2

num = int(input())

s = 0
i = 10

while num >= 1:
    s += num % i
    num //= i

point = int(s % i)
print(point)
