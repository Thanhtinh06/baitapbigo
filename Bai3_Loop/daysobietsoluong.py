
# n = int(input())

# count = 0
# for i in range(n):
#     x = int(input())
#     print(x, end=" ")


# stop 0


min = 11
max = -1

while True:
    x = int(input())
    if x == -1:
        break
    if x < min and min > -1:
        min = x
    if x > max and max < 11:
        max = x

print(max, min, end=" ")
