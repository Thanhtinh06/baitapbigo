def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        else:
            return True


n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(n):
    if isPrime(a[i]):
        count += 1

print(count)
