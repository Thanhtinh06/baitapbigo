import math

# a, b, c = input().split()

# P = float(a) + float(b) + float(c)
# p = P / 2
# S = math.sqrt(p * (p - float(a)) * (p - float(b))*(p - float(c)))

# print('%.2f %.2f' % (P, S))


# cach 2

a, b, c = map(float, input().split())

P = a + b + c
p = P / 2
S = (p * (p-a) * (p-b) * (p-c)) ** 0.5

print('%.2f %.2f' % (P, S))
