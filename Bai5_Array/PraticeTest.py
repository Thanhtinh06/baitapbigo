n = int(input())
arr = list(map(int, input().split()))

result = n
for num in arr:
  if num % 10 == 0 and num < result and num >= 0:
    result = num

print(result)
