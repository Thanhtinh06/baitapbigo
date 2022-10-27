n = int(input())
a = list(map(int, input().split()))

min_a = min(a)
power = 0

for i in range(n):
    power_i = a[i] - min_a
    if power_i > 0:
        power += power_i

print(power)
