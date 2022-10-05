m, n, a = map(int, input().split())

weight = m // a
height = n // a

if m % a != 0:
    weight += 1
if n % a != 0:
    height += 1

count = weight * height

print(count)
